from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.single_product, name='single_product'),

    path('admin/products/', views.admin_product_list, name='admin_product_list'),
    path('admin_product_add', views.admin_product_add, name='admin_product_add'),
    path('admin/products/update/<int:product_id>/', views.admin_product_update, name='admin_product_update'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
