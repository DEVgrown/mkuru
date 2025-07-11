from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomerUserForm, CustomerForm
from .models import Customer
from mkuru.models import Order

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def customerregister(request):
    if request.method == 'POST':
        user_form = CustomerUserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if user_form.is_valid() and customer_form.is_valid():
            print("Forms are valid!")
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.email = customer_form.cleaned_data['email']
            customer.save()
            
            # Add user to CUSTOMER group
            group = Group.objects.get(name='CUSTOMER')
            user.groups.add(group)
            
            # Also add the group to the customer model
            customer.groups.add(group)
            
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('customerlogin')
        else:
            messages.error(request, 'Registration failed. Please check your input.')
            
    else:
        user_form = CustomerUserForm()
        customer_form = CustomerForm()
        
    return render(request, 'registration/login.html', {
        'user_form': user_form, 
        'customer_form': customer_form
    })

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

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
    # Try to find a Customer record matching the logged-in user
    customer = Customer.objects.filter(user=user).first()
    orders = []
    if customer:
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    context = {
        'user': user,
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'customer/customer_dashboard.html', context)

