from django.urls import path

from .views import (moysklad,
    get_counterparties, create_counterparty, update_counterparty, delete_counterparty,
    get_products, create_product, update_product, delete_product,
    get_customer_orders, create_customer_order, update_customer_order, delete_customer_order,
    get_purchase_orders, create_purchase_order, 
    get_invoices, create_invoice, update_invoice, delete_invoice,
    get_stores, create_store, update_store, delete_store,
    get_organizations, create_organization
)

urlpatterns = [
    path('', moysklad, name='moysklad'),
    # Counterparty URLs
    path('counterparties/', get_counterparties, name='get_counterparties'),
    path('counterparties/create/', create_counterparty, name='create_counterparty'),
    path('counterparties/update/<str:counterparty_id>/', update_counterparty, name='update_counterparty'),
    path('counterparties/delete/<str:counterparty_id>/', delete_counterparty, name='delete_counterparty'),

    # Product URLs
    path('products/', get_products, name='get_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/update/<str:product_id>/', update_product, name='update_product'),
    path('products/delete/<str:product_id>/', delete_product, name='delete_product'),

    # Customer Order URLs
    path('customer-orders/', get_customer_orders, name='get_customer_orders'),
    path('customer-orders/create/', create_customer_order, name='create_customer_order'),
    path('customer-orders/update/<str:order_id>/', update_customer_order, name='update_customer_order'),
    path('customer-orders/delete/<str:order_id>/', delete_customer_order, name='delete_customer_order'),

    # Purchase Order URLs
    path('purchase-orders/', get_purchase_orders, name='get_purchase_orders'),
    path('purchase-orders/create/', create_purchase_order, name='create_purchase_order'),
    # path('purchase-orders/update/<str:order_id>/', update_purchase_order, name='update_purchase_order'),
    # path('purchase-orders/delete/<str:order_id>/', delete_purchase_order, name='delete_purchase_order'),

    # Invoice URLs
    path('invoices/', get_invoices, name='get_invoices'),
    path('invoices/create/', create_invoice, name='create_invoice'),
    path('invoices/update/<str:invoice_id>/', update_invoice, name='update_invoice'),
    path('invoices/delete/<str:invoice_id>/', delete_invoice, name='delete_invoice'),

    # Store URLs
    path('stores/', get_stores, name='get_stores'),
    path('stores/create/', create_store, name='create_store'),
    path('stores/update/<str:store_id>/', update_store, name='update_store'),
    path('stores/delete/<str:store_id>/', delete_store, name='delete_store'),

    # Organization URLs
    path('organizations/', get_organizations, name='get_organizations'),
    # path('organizations/create/', create_organization, name='create_organization'),
    # path('organizations/update/<str:organization_id>/', update_organization, name='update_organization'),
    # path('organizations/delete/<str:organization_id>/', delete_organization, name='delete_organization'),

    # # Stock URLs
    # path('stock/by-store/', get_stock_by_store, name='get_stock_by_store'),
    # path('stock/current-by-store/', get_current_stock_by_store, name='get_current_stock_by_store'),
]