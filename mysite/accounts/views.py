from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages

def login_view(request):
    login_form = AuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        # Determine which form was submitted (e.g., by checking for a specific field)
        if 'login_submit' in request.POST: # Assuming a submit button named 'login_submit' in the login form
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f'You are now logged in as {username}.')
                    # Redirect based on user role
                    if user.role == 'admin':
                        return redirect('admin_dashboard')
                    elif user.role == 'cashier':
                        return redirect('cashier_dashboard')
                    elif user.role == 'customer':
                        return redirect('customer_dashboard')
                    else:
                        return redirect(getattr(settings, 'LOGIN_REDIRECT_URL', '/'))
                else:
                    messages.error(request, 'Invalid username or password.')
        elif 'register_submit' in request.POST: # Assuming a submit button named 'register_submit' in the registration form
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                # Optional: Log the user in after registration
                # login(request, user)
                messages.success(request, 'Registration successful. Please log in.')
                # Redirect to the same page or a login success page
                return redirect('login_register') # Redirect back to the same page to show the login form
            else:
                messages.error(request, 'Registration failed. Please check your input.')

    # Render the template with both forms
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

def customer_dashboard_view(request):
    # Add logic to check if the user is a Customer and render customer dashboard template
    return render(request, 'accounts/customer_dashboard.html')

