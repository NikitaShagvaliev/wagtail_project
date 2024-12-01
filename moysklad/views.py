from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from .entities.MoySkladApi import *

# Замените ваши логин и пароль на реальные, но только для тестирования!
# В продакшне используйте OAuth 2.0!
MOYSKLAD_LOGIN = "admin@egort123"
MOYSKLAD_PASSWORD = "egor86"
MOYSKLAD_BASE_URL =  "https://api.moysklad.ru/api/remap/1.2" # Замените на ваш базовый URL

def moysklad(request):
    return render(request, 'moysklad/moysklad.html')

def get_moysklad_client(entity_client_class):
    return entity_client_class(MOYSKLAD_LOGIN, MOYSKLAD_PASSWORD, MOYSKLAD_BASE_URL, verify_ssl=False)


def handle_api_request(request, client, method, id=None, data=None):
    try:
        if method == 'GET':
            response_data = client.get(id)
        elif method == 'POST':
            response_data = client.post(data)
        elif method == 'PUT':
            response_data = client.put(id, data)
        elif method == 'DELETE':
            client.delete(id)
            return JsonResponse({"success": True})
        else:
            return HttpResponseBadRequest("Invalid request method")
        return JsonResponse(response_data)
    except Exception as e:
        print(f"Error during API request: {e}")
        return HttpResponseServerError(f"API request failed: {e}")


# Customer Order Views

def get_customer_orders(request):
    client = get_moysklad_client(CustomerOrderClient)
    return handle_api_request(request, client, 'GET')

def create_customer_order(request):
    if request.method == "POST":
        try:
            data = {
                'organization': request.POST.get('organization'),
                'agent': request.POST.get('agent'),
                'positions': request.POST.get('positions') #Это нужно парсить в json, если positions - это JSON строка
            }
            client = get_moysklad_client(CustomerOrderClient)
            return handle_api_request(request, client, 'POST', data=data)
        except Exception as e:
            return HttpResponseBadRequest(f"Invalid request data: {e}")
    else:
        return HttpResponseBadRequest("Invalid request method")

def update_or_delete_customer_order(request, order_id):
    client = get_moysklad_client(CustomerOrderClient)
    if request.method == "PUT":
        try:
            data = {
                'organization': request.POST.get('organization'),
                'agent': request.POST.get('agent'),
                'positions': request.POST.get('positions') #Это нужно парсить в json, если positions - это JSON строка
            }
            return handle_api_request(request, client, 'PUT', id=order_id, data=data)
        except Exception as e:
            return HttpResponseBadRequest(f"Invalid request data: {e}")
    elif request.method == "DELETE":
        return handle_api_request(request, client, 'DELETE', id=order_id)
    else:
        return HttpResponseBadRequest("Invalid request method")


# Counterparty Views
def get_counterparties(request):
    client = get_moysklad_client(CounterpartyClient)
    return handle_api_request(request, client, 'GET')

def create_counterparty(request):
    if request.method == "POST":
        try:
            data = {
                "name": request.POST.get("name"),
                "phone": request.POST.get("phone"),
                "email": request.POST.get("email"),
            }
            client = get_moysklad_client(CounterpartyClient)
            return handle_api_request(request, client, 'POST', data=data)
        except Exception as e:
            return HttpResponseBadRequest(f"Invalid data: {e}")
    else:
        return HttpResponseBadRequest("Invalid request method")

def update_or_delete_counterparty(request, counterparty_id):
    client = get_moysklad_client(CounterpartyClient)
    if request.method == "PUT":
        try:
            data = {
                "name": request.POST.get("name"),
                "phone": request.POST.get("phone"),
                "email": request.POST.get("email"),
            }
            return handle_api_request(request, client, 'PUT', id=counterparty_id, data=data)
        except Exception as e:
            return HttpResponseBadRequest(f"Invalid data: {e}")
    elif request.method == "DELETE":
        return handle_api_request(request, client, 'DELETE', id=counterparty_id)
    else:
        return HttpResponseBadRequest("Invalid request method")


# ... аналогично для остальных сущностей ...