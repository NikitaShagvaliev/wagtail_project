from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
]