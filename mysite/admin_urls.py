from django.urls import path
from . import admin_views

urlpatterns = [
    path('admin/products/', admin_views.product_list, name='admin_product_list'),
    path('admin/products/add/', admin_views.product_add, name='admin_product_add'),
    path('admin/products/update/<int:product_id>/', admin_views.product_update, name='admin_product_update'),
]