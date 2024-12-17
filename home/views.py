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

# Отключаем предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def contacts(request):
    return render(request, 'home/contacts.html')

def index(request):
    return render(request, 'home/index.html')

def company(request):
    return render(request, 'home/company.html')

def delivery(request):
    return render(request, 'home/delivery.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def catalog(request):
    url = "http://127.0.0.1:8000//moysklad/products/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('rows', [])
        
        # Добавляем изображения для каждого продукта
        for product in products:
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
        
        # Пагинация
        paginator = Paginator(products, 6)  # Показывать по 10 товаров на странице
        page = request.GET.get('page')  # Получаем текущую страницу из GET-параметра
        
        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, возвращаем первую страницу
            products_page = paginator.page(1)
        except EmptyPage:
            # Если страница выходит за пределы допустимого диапазона, возвращаем последнюю страницу
            products_page = paginator.page(paginator.num_pages)
        
        context = {'products': products_page}
        return render(request, 'home/catalog.html', context)
    
    return render(request, 'home/catalog.html', {'products': []})


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

def catalog_id(request, product_id):
    context = {}  
    url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        product_data = response.json()
        context["product"] = product_data
        images_url = product_data.get('images', {}).get('meta', {})
        images_url = images_url.get('href')
        # Если ссылка на изображения существует, выполняем запрос
        print(images_url)
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

def extract_uuid_from_href(href):
    import re
    # Регулярное выражение для поиска UUID
    match = re.search(r'/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/?$', href)
    if match:
        return match.group(1)  # Возвращаем UUID
    return None

def contacts(request):
    return render(request, 'home/contacts.html')










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

def checkout(request):
    if request.method == "POST":
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price for item in cart_items)

        # Данные для оплаты
        payment_data = {
            "id": f"order_{request.user.id}_{cart_items.first().id}",
            "from": {
                "accountNumber": "12345678900987654321",
            },
            "to": {
                "accountNumber": "98765432100123456789",
                "inn": "1234567890",
                "kpp": "123456789",
                "bankBic": "044525225",
                "bankName": "Банк получателя",
                "bankCorrAccount": "30101810400000000225",
            },
            "purpose": f"Оплата заказа от {request.user.username}",
            "amount": float(total_amount),
            "dueDate": "2024-12-31T23:59:59+03:00",
        }

        # Отправка данных на оплату через API Т-Банка
        response = TBankService.perform_payment(payment_data)

        if response and response.get("status") == "success":
            # Очистка корзины после успешной оплаты
            cart_items.delete()
            return redirect(response.get("redirect_url"))
        else:
            return JsonResponse({"error": "Ошибка при выполнении платежа"}, status=500)
    else:
        return JsonResponse({"error": "Метод не поддерживается"}, status=405)

def add_to_cart(request, product_id):
    
    # Добавляем товар в корзину (в сессии)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id))
    if cart_item:
        cart_item['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'id': product_id,
            'name': f"Товар {product_id}",  # Упрощенное имя товара
            'price': 100.00,  # Упрощенная цена товара
            'quantity': 1,
        }
    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_amount = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'home/cart.html', {
        'cart': cart,
        'total_amount': total_amount,
    })

from django.shortcuts import render, get_object_or_404

def product_detail(request, product_id):
    """
    Представление для отображения деталей товара.
    """
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'home/product_detail.html', {'product': product})