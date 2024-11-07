from django.shortcuts import render
from django.http import JsonResponse
from .oauth import MoySkladOAuth
from .entities.counterparty import CounterpartyClient
from .entities.product import ProductClient
from .entities.customer_order import CustomerOrderClient
from .entities.purchase_order import PurchaseOrderClient
from .entities.invoice import InvoiceClient
from .entities.store import StoreClient
from .entities.organization import OrganizationClient
from .entities.stock import StockClient

# Customer Order Views
def get_customer_orders(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = CustomerOrderClient(access_token)
    orders = api_client.get_customer_orders()
    return JsonResponse(orders)

def create_customer_order(request):
    if request.method == "POST":
        organization = request.POST.get("organization")
        agent = request.POST.get("agent")
        positions = request.POST.get("positions")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CustomerOrderClient(access_token)
        new_order = api_client.create_customer_order(organization, agent, positions)
        return JsonResponse(new_order)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_customer_order(request, order_id):
    if request.method == "PUT":
        organization = request.POST.get("organization")
        agent = request.POST.get("agent")
        positions = request.POST.get("positions")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CustomerOrderClient(access_token)
        updated_order = api_client.update_customer_order(order_id, organization, agent, positions)
        return JsonResponse(updated_order)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_customer_order(request, order_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CustomerOrderClient(access_token)
        success = api_client.delete_customer_order(order_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete customer order"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Purchase Order Views
def get_purchase_orders(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = PurchaseOrderClient(access_token)
    orders = api_client.get_purchase_orders()
    return JsonResponse(orders)

def create_purchase_order(request):
    if request.method == "POST":
        organization = request.POST.get("organization")
        agent = request.POST.get("agent")
        positions = request.POST.get("positions")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token
def get_counterparties(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = CounterpartyClient(access_token)
    counterparties = api_client.get_counterparties()
    return JsonResponse(counterparties)

def create_counterparty(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CounterpartyClient(access_token)
        new_counterparty = api_client.create_counterparty(name, phone, email)
        return JsonResponse(new_counterparty)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_counterparty(request, counterparty_id):
    if request.method == "PUT":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CounterpartyClient(access_token)
        updated_counterparty = api_client.update_counterparty(counterparty_id, name, phone, email)
        return JsonResponse(updated_counterparty)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_counterparty(request, counterparty_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = CounterpartyClient(access_token)
        success = api_client.delete_counterparty(counterparty_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete counterparty"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def get_products(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = ProductClient(access_token)
    products = api_client.get_products()
    return JsonResponse(products)

def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        description = request.POST.get("description")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = ProductClient(access_token)
        new_product = api_client.create_product(name, code, description)
        return JsonResponse(new_product)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_product(request, product_id):
    if request.method == "PUT":
        name = request.POST.get("name")
        code = request.POST.get("code")
        description = request.POST.get("description")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = ProductClient(access_token)
        updated_product = api_client.update_product(product_id, name, code, description)
        return JsonResponse(updated_product)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_product(request, product_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = ProductClient(access_token)
        success = api_client.delete_product(product_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete product"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Invoice Views
def get_invoices(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = InvoiceClient(access_token)
    invoices = api_client.get_invoices()
    return JsonResponse(invoices)

def create_invoice(request):
    if request.method == "POST":
        organization = request.POST.get("organization")
        agent = request.POST.get("agent")
        positions = request.POST.get("positions")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = InvoiceClient(access_token)
        new_invoice = api_client.create_invoice(organization, agent, positions)
        return JsonResponse(new_invoice)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_invoice(request, invoice_id):
    if request.method == "PUT":
        organization = request.POST.get("organization")
        agent = request.POST.get("agent")
        positions = request.POST.get("positions")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = InvoiceClient(access_token)
        updated_invoice = api_client.update_invoice(invoice_id, organization, agent, positions)
        return JsonResponse(updated_invoice)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_invoice(request, invoice_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = InvoiceClient(access_token)
        success = api_client.delete_invoice(invoice_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete invoice"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Store Views
def get_stores(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = StoreClient(access_token)
    stores = api_client.get_stores()
    return JsonResponse(stores)

def create_store(request):
    if request.method == "POST":
        name = request.POST.get("name")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = StoreClient(access_token)
        new_store = api_client.create_store(name)
        return JsonResponse(new_store)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_store(request, store_id):
    if request.method == "PUT":
        name = request.POST.get("name")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = StoreClient(access_token)
        updated_store = api_client.update_store(store_id, name)
        return JsonResponse(updated_store)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_store(request, store_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = StoreClient(access_token)
        success = api_client.delete_store(store_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete store"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Organization Views
def get_organizations(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = OrganizationClient(access_token)
    organizations = api_client.get_organizations()
    return JsonResponse(organizations)

def create_organization(request):
    if request.method == "POST":
        name = request.POST.get("name")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = OrganizationClient(access_token)
        new_organization = api_client.create_organization(name)
        return JsonResponse(new_organization)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def update_organization(request, organization_id):
    if request.method == "PUT":
        name = request.POST.get("name")

        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = OrganizationClient(access_token)
        updated_organization = api_client.update_organization(organization_id, name)
        return JsonResponse(updated_organization)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def delete_organization(request, organization_id):
    if request.method == "DELETE":
        oauth = MoySkladOAuth("your_client_id", "your_client_secret")
        access_token = oauth.get_token()
        api_client = OrganizationClient(access_token)
        success = api_client.delete_organization(organization_id)
        if success:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Failed to delete organization"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Stock Views
def get_stock_by_store(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = StockClient(access_token)
    stock = api_client.get_stock_by_store()
    return JsonResponse(stock)

def get_current_stock_by_store(request):
    oauth = MoySkladOAuth("your_client_id", "your_client_secret")
    access_token = oauth.get_token()
    api_client = StockClient(access_token)
    stock = api_client.get_current_stock_by_store()
    return JsonResponse(stock)