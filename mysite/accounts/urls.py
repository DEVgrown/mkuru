# mysite/accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login'), # Using our custom login_view
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # Django's built-in logout view
    # You can add more URLs for password reset, etc. here
]