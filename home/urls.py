from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<str:category>/', views.catalog_category, name='catalog_category'),
    path('catalog/id/<str:product_id>/', views.product_detail, name='product_detail'),  # Используйте UUID
    path('add-to-cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
]