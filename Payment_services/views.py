from django.shortcuts import render

def index(request):
    return render(request, 'Payment_services/Payment_services.html')