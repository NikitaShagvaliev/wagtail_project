from django.urls import path
from .views import *

urlpatterns = [
    path('', moysklad, name='moysklad'),
    
    path('customer-orders/', get_customer_orders, name='get_customer_orders'),
    path('customer-orders/create/', create_customer_order, name='create_customer_order'),
    path('customer-orders/<int:order_id>/', update_or_delete_customer_order, name='update_or_delete_customer_order'),

    # ...  Добавьте аналогичные пути для других сущностей ...

    path('counterparties/', get_counterparties, name='get_counterparties'),
    path('counterparties/create/', create_counterparty, name='create_counterparty'),
    path('counterparties/<int:counterparty_id>/', update_or_delete_counterparty, name='update_or_delete_counterparty'),

    # path('products/', get_products, name='get_products'),
    # path('products/create/', create_product, name='create_product'),
    # path('products/<int:product_id>/', update_or_delete_product, name='update_or_delete_product'),

    # ... и так далее для всех сущностей ...
]