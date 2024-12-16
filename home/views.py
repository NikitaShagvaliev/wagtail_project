from django.shortcuts import render
import requests
from moysklad.views import get_products
import base64
import urllib3

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