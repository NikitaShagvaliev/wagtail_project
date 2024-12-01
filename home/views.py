from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def company(request):
    return render(request, 'home/company.html')

def delivery(request):
    return render(request, 'home/delivery.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def catalog(request):
    return render(request, 'home/catalog.html')