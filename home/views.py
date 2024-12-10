from django.shortcuts import render
import requests
from moysklad.views import get_products

import urllib3

# Отключаем предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def index(request):
    return render(request, 'home/index.html')

def company(request):
    return render(request, 'home/page39291702body.html')

def delivery(request):
    return render(request, 'home/delivery.html')

def catalog(request):
    url = "http://127.0.0.1:8000//moysklad/products/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('rows', [])
        context = {'products': products}
        return render(request, 'home/catalog.html', context)
    return render(request, 'home/catalog.html', {'products': []})

def catalog_category(request, category):
    url = "http://127.0.0.1:8000//moysklad/products/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('rows', [])
        # Фильтруем продукты по значению "pathName"
        sale_products = [product for product in products if product.get('pathName') == category]
        context = {'products': sale_products}
        return render(request, 'home/catalog.html', context)
    return render(request, 'home/catalog.html', {'products': []})

def catalog_id(request, product_id):
    url = f"http://127.0.0.1:8000//moysklad/products/{product_id}/"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        product_data = response.json()
        context = {'product': product_data}
        return render(request, 'home/product_detail.html', context)
    return render(request, 'home/product_detail.html', {'product': None})

def contacts(request):
    return render(request, 'home/contacts.html')