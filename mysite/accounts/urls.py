# mysite/accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('customerregister/', views.customerregister, name='customerregister'),
    path('customerlogin/', LoginView.as_view(template_name='registration/login.html'), name='customerlogin'),
    path('customer_dashboard/', views.customer_dashboard_view, name='customer_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # You can add more URLs for password reset, etc. here
]