from django.shortcuts import render
import requests
from moysklad.views import get_products
import base64
import urllib3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, CartItem
from Payment_services.tbank_service import TBankService
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder
# Отключаем предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def contacts(request):
    return render(request, 'home/contacts.html')

def index(request):
    # Определяем категорию (бренды), которые вы хотите отобразить
    category = "popular brands"
    context = {}
    # Проверяем, есть ли данные в сессии
    if 'products_data_index' in request.session and 'product_ids_index' in request.session:
        # Получаем данные из сессии
        products_data = json.loads(request.session['products_data_index'])
        products = products_data.get('rows', [])
        session_product_ids = set(request.session['product_ids_index'])

        # Выполняем запрос к МойСклад для проверки актуальности данных
        url = "http://127.0.0.1:8000//moysklad/products/"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            new_products_data = response.json()
            new_products = new_products_data.get('rows', [])
            new_product_ids = {product['id'] for product in new_products}

            # Проверяем, совпадает ли количество ID
            if len(session_product_ids) == len(new_product_ids):
                # Если количество ID совпадает, используем данные из сессии
                print("Используем данные из сессии")
                filtered_products = [product for product in products if product.get('pathName') == category]
                grouped_products = [filtered_products[i:i + 4] for i in range(0, len(filtered_products), 4)]

                sales_hits_products_3 = [product for product in products if product.get('pathName') == 'sales_hits'][:3]
                new_products_products_3 = [product for product in products if product.get('pathName') == 'new_products'][:3]

                # Загружаем изображения для sales_hits_products_3 и new_products_products_3
                for products_list in [sales_hits_products_3, new_products_products_3]:
                    for product in products_list:
                        product_id = product.get('id')
                        if 'image_base64' not in product:  # Проверяем, есть ли изображение
                            images_url = product.get('images', {}).get('meta', {}).get('href')
                            if images_url:
                                url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images"
                                images_response = requests.get(url, verify=False)
                                if images_response.status_code == 200:
                                    images_data = images_response.json()
                                    if images_data.get('rows'):
                                        first_image_meta = images_data.get('rows', [])[0].get('meta', {}).get('href')
                                        id_images = extract_uuid_from_href(first_image_meta)
                                        if id_images:
                                            url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images/{id_images}"
                                            image_response = requests.get(url, verify=False)
                                            if image_response.status_code == 200:
                                                image_base64 = base64.b64encode(image_response.content).decode('utf-8')
                                                product['image_base64'] = image_base64  # Добавляем изображение в словарь продукта

                # Объединяем все данные в контекст
                context = {
                    'grouped_products': grouped_products,
                    'sales_hits_products_3': sales_hits_products_3,
                    'new_products_products_3': new_products_products_3,
                }

                return render(request, 'home/index.html', context)
            else:
                print("Количество ID не совпадает, загружаем данные заново")
                # Если количество ID не совпадает, используем новые данные
                products_data = new_products_data
                products = new_products
        else:
            print(f"Ошибка при запросе к МойСклад: {response.status_code}")
            return render(request, 'home/index.html', {'products': []})
    else:
        print("Данные в сессии отсутствуют, загружаем данные заново")
        # Если данных в сессии нет, выполняем запрос к МойСклад
        url = "http://127.0.0.1:8000//moysklad/products/"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            products_data = response.json()
            products = products_data.get('rows', [])
        else:
            print(f"Ошибка при запросе к МойСклад: {response.status_code}")
            return render(request, 'home/index.html', {'products': []})

    # Фильтруем продукты по значению "pathName"
    filtered_products = [product for product in products if product.get('pathName') == category]
    grouped_products = [filtered_products[i:i + 4] for i in range(0, len(filtered_products), 4)]

    sales_hits_products_3 = [product for product in products if product.get('pathName') == 'sales_hits'][:3]
    new_products_products_3 = [product for product in products if product.get('pathName') == 'new_products'][:3]

    # Добавляем изображения для каждого продукта из sales_hits_products_3 и new_products_products_3
    for products_list in [sales_hits_products_3, new_products_products_3]:
        for product in products_list:
            product_id = product.get('id')
            images_url = product.get('images', {}).get('meta', {}).get('href')
            if images_url:
                url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images"
                images_response = requests.get(url, verify=False)
                if images_response.status_code == 200:
                    images_data = images_response.json()
                    if images_data.get('rows'):
                        first_image_meta = images_data.get('rows', [])[0].get('meta', {}).get('href')
                        id_images = extract_uuid_from_href(first_image_meta)
                        if id_images:
                            url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images/{id_images}"
                            image_response = requests.get(url, verify=False)
                            if image_response.status_code == 200:
                                image_base64 = base64.b64encode(image_response.content).decode('utf-8')
                                product['image_base64'] = image_base64  # Добавляем изображение в словарь продукта

    # Объединяем все данные в контекст
    context = {
        'grouped_products': grouped_products,
        'sales_hits_products_3': sales_hits_products_3,
        'new_products_products_3': new_products_products_3,
    }

    # Сохраняем данные в сессии
    request.session['products_data_index'] = json.dumps(products_data, cls=DjangoJSONEncoder)
    request.session['product_ids_index'] = list({product['id'] for product in products})
    request.session.save()

    return render(request, 'home/index.html', context)

def company(request):
    return render(request, 'home/company.html')

def delivery(request):
    return render(request, 'home/delivery.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def catalog(request):
    # Выполняем запрос к МойСклад только если данных в сессии нет или они устарели
    url = "http://127.0.0.1:8000//moysklad/products/"
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        new_products_data_catalog = response.json()
        new_products = new_products_data_catalog.get('rows', [])
        new_product_ids_catalog = {product['id'] for product in new_products}
        flag = 'products_data_catalog' in request.session
        
        if flag:
            print('сессия')
            # Если данные в сессии есть, сравниваем ID
            products_data_catalog = json.loads(request.session['products_data_catalog'])
            products = products_data_catalog.get('rows', [])
            product_ids_catalog = set(request.session.get('product_ids_catalog', []))
            
            # Находим новые и удаленные ID
            new_ids = new_product_ids_catalog - product_ids_catalog
            deleted_ids = product_ids_catalog - new_product_ids_catalog
            
            # Находим новые товары по их ID
            new_products_to_process = [product for product in new_products if product['id'] in new_ids]
            print(f"Новые продукты: {len(new_products_to_process)}")
            
            # Удаляем продукты с удаленными ID
            products_all = [product for product in products if product['id'] not in deleted_ids]
            print(f"Старые продукты: {len(products_all)}")
            
            # Объединяем старые и новые товары
            products_all.extend(new_products_to_process)
            products = products_all  # Обновляем products для пагинации
        else:
            # Если данных в сессии нет, сохраняем новые данные
            print('сам по себе заново')
            products = new_products
            request.session['products_data_catalog'] = json.dumps({'rows': products}, cls=DjangoJSONEncoder)
            request.session['product_ids_catalog'] = list(new_product_ids_catalog)
        
        # Обновляем время последнего обновления
        request.session['last_update_catalog'] = timezone.now().isoformat()
        request.session.save()
    else:
        print("Ошибка при запросе к МойСклад")  # Отладочное сообщение
        return render(request, 'home/catalog.html', {'products': []})

    # Инициализируем словарь для хранения изображений в сессии
    request.session['image_base64'] = request.session.get('image_base64', {})

    # Добавляем изображения для каждого продукта, если они еще не были добавлены
    product_ids_catalog = set(request.session.get('product_ids_catalog', []))
    for product in products:
        product_id = product.get('id')
        print(f"ID продукта: {product_id}")
        if product_id not in request.session['image_base64']:  # Проверяем, есть ли изображение в сессии
            print('Загружаем изображение')
            images_url = product.get('images', {}).get('meta', {}).get('href')
            if images_url:
                url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images"
                images_response = requests.get(url, verify=False)
                
                if images_response.status_code == 200:
                    images_data = images_response.json()
                    if images_data.get('rows'):
                        first_image_meta = images_data.get('rows', [])[0].get('meta', {}).get('href')
                        id_images = extract_uuid_from_href(first_image_meta)
                        if id_images:
                            url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images/{id_images}"
                            image_response = requests.get(url, verify=False)
                            if image_response.status_code == 200:
                                image_base64 = base64.b64encode(image_response.content).decode('utf-8')
                                # Сохраняем изображение в сессии
                                request.session['image_base64'][product_id] = image_base64
                                product['image_base64'] = image_base64  # Добавляем изображение в словарь продукта

    # Если данные в сессии обновлялись, сохраняем их
    if flag:
        print(f"Обновленные продукты: {len(products)}")
        # Сохраняем данные в сессии
        request.session['products_data_catalog'] = json.dumps({'rows': products}, cls=DjangoJSONEncoder)
        request.session['product_ids_catalog'] = list({product['id'] for product in products})
        request.session.save()  # Сохраняем изменения

    # Пагинация
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)
    
    context = {
        'products': products_page,
        'image_base64': request.session.get('image_base64', {}),
    }
    return render(request, 'home/catalog.html', context)

def catalog_category(request, category):
    url = "http://127.0.0.1:8000//moysklad/products/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('rows', [])
        
        # Фильтруем продукты по значению "pathName"
        filtered_products = [product for product in products if product.get('pathName') == category]
        
        # Добавляем изображения для каждого продукта
        for product in filtered_products:
            product_id = product.get('id')
            images_url = product.get('images', {}).get('meta', {}).get('href')
            
            if images_url:
                # Получаем список изображений
                url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images"
                images_response = requests.get(url, verify=False)
                
                if images_response.status_code == 200:
                    images_data = images_response.json()
                    if images_data.get('rows'):
                        # Получаем первое изображение
                        first_image_meta = images_data.get('rows', [])[0].get('meta', {}).get('href')
                        id_images = extract_uuid_from_href(first_image_meta)
                        
                        if id_images:
                            # Получаем изображение в формате Base64
                            url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images/{id_images}"
                            image_response = requests.get(url, verify=False)
                            
                            if image_response.status_code == 200:
                                image_base64 = base64.b64encode(image_response.content).decode('utf-8')
                                product['image_base64'] = image_base64  # Добавляем изображение в словарь продукта
        
        context = {'products': filtered_products}
        return render(request, 'home/catalog.html', context)
    return render(request, 'home/catalog.html', {'products': []})

def extract_uuid_from_href(href):
    import re
    # Регулярное выражение для поиска UUID
    match = re.search(r'/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/?$', href)
    if match:
        return match.group(1)  # Возвращаем UUID
    return None

def contacts(request):
    return render(request, 'home/contacts.html')


def catalog_id(request, product_id):
    context = {}  
    url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        product_data = response.json()
        context["product"] = product_data
        images_url = product_data.get('images', {}).get('meta', {})
        images_url = images_url.get('href')
        if images_url:
            # для получения id_images
            url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images"
            images_response = requests.get(url, verify=False)
            
            product_data = images_response.json()
            if product_data.get('rows'):
                product_data = product_data.get('rows', [])[0].get('meta', {}).get('href')
                id_images = extract_uuid_from_href(product_data)
            
                # # изображения
                url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/images/{id_images}"
                images_response = requests.get(url, verify=False)
                import base64
                image_base64 = base64.b64encode(images_response.content).decode('utf-8')
                context["img"] = image_base64  # Сохраняем Base64-строку в контекст
        # Передаем данные в шаблон
        return render(request, 'home/product_detail.html', context)
    return render(request, 'home/product_detail.html', {'product': None})








def view_cart(request):
    """
    Представление для отображения корзины.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.total_price for item in cart_items)
    return render(request, "home/view_cart.html", {
        "cart_items": cart_items,
        "total_amount": total_amount,
    })
import logging

logger = logging.getLogger(__name__)

def checkout(request):
    if request.method == "POST":
        cart = request.session.get('cart', {})
        
        if not cart:
            return JsonResponse({"error": "Корзина пуста"}, status=400)
        
        total_amount = sum(item['price'] * item['quantity'] for item in cart.values())

        # Подготовка данных в правильном формате
        payment_data = {
            "id": "unique_payment_id_123",
            "from": {
                "accountNumber": "12345678901234567890"
            },
            "to": {
                "name": "ООО Получатель",
                "inn": "7707083893",  # Исправленный ИНН
                "kpp": "123456789",
                "bik": "044525225",
                "bankName": "Банк Получателя",
                "corrAccountNumber": "30101810400000000225",
                "accountNumber": "98765432109876543210"
            },
            "purpose": "Оплата заказа №123",
            "amount": float(total_amount),  # Убедитесь, что сумма корректная
            "dueDate": "2024-12-25T12:00:00Z"
        }

        # Выполнение платежа через TBankService
        result = TBankService.perform_payment(payment_data)
        print(result)  # Для отладки

        if result:
            # Если платеж выполнен успешно
            request.session['cart'] = {}  # Очищаем корзину
            return JsonResponse({
                "message": "Платеж успешно выполнен",
                "details": result
            }, status=200)
        else:
            # Если произошла ошибка
            return JsonResponse({
                "error": "Ошибка при выполнении платежа",
                "details": result
            }, status=500)
            
    return JsonResponse({"error": "Метод не поддерживается"}, status=405)
            
def add_to_cart(request, product_id):
    context = {}  
    url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        product_data = response.json()
        context["product"] = product_data
    print(context)
    
    
    # Добавляем товар в корзину (в сессии)
    cart = request.session.get('cart', {})
    
    cart_item = cart.get(product_id)
   
    if cart_item:
        cart_item['quantity'] += 1
    else:
        # Используем динамическое имя из JSON
        product_name = context["product"].get("name", f"Товар {product_id}")
        product_price = context["product"].get("salePrices", [{}])[0].get("value", 100.00)  # Берем цену напрямую
        
        cart[product_id] = {
            'id': product_id,
            'name': product_name,  # Динамическое имя из JSON
            'price': product_price,  # Цена из API
            'quantity': 1,
        }
    print(cart_item)
    request.session['cart'] = cart
    return redirect('view_cart')



def view_cart(request):
    cart = request.session.get('cart', {})
    
    # Преобразуем корзину в список товаров для отображения
    cart_items = []
    total_amount = 0
    for item_id, item in cart.items():
        item['total_price'] = item['price'] * item['quantity']  # Рассчитываем итоговую стоимость
        cart_items.append(item)
        total_amount += item['total_price']  # Суммируем итоговую стоимость
    
    # Передаем данные в шаблон
    return render(request, 'home/cart.html', {
        'cart_items': cart_items,  # Передаем список товаров
        'total_amount': total_amount,  # Передаем итоговую сумму
    })

from django.shortcuts import render, get_object_or_404

