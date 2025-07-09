from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from mkuru.models import Customer, Order
from django.contrib.auth.decorators import login_required

def login_view(request):
    login_form = AuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            # Custom logic to allow login with username or email
            login_value = request.POST.get('login')
            password = request.POST.get('password')
            user = None
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if login_value:
                # Try to authenticate by username
                user_qs = User.objects.filter(username=login_value)
                if user_qs.exists():
                    user = authenticate(request, username=login_value, password=password)
                else:
                    # Try to authenticate by email
                    try:
                        user_obj = User.objects.get(email=login_value)
                        user = authenticate(request, username=user_obj.username, password=password)
                    except User.DoesNotExist:
                        user = None
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {user.username}.')
                return redirect('customer_dashboard')
            else:
                messages.error(request, 'Invalid username/email or password.')
        elif 'register_submit' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Registration failed. Please check your input.')

    return render(request, 'customer/login.html', {
        'login_form': login_form,
        'register_form': register_form,
    })
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return redirect('home') # Redirect to your home page after logout

# Placeholder views for dashboards - replace with your actual dashboard views
def admin_dashboard_view(request):
    # Add logic to check if the user is an Admin and render admin dashboard template
    return render(request, 'accounts/admin_dashboard.html')

def cashier_dashboard_view(request):
    # Add logic to check if the user is a Cashier and render cashier dashboard template
    return render(request, 'accounts/cashier_dashboard.html')

@login_required
def customer_dashboard_view(request):
    user = request.user
    # Try to find a Customer record matching the logged-in user's email
    customer = Customer.objects.filter(email=user.email).first()
    orders = []
    if customer:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    context = {
        'user': user,
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'customer/customer_dashboard.html', context)

