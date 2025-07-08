from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)



def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'admin/products/product_list.html', {'products': products})

def admin_product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')  # Redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'admin/products/product_add.html', {'form': form})

def admin_product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')  # Redirect to the product list page
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin/products/product_update.html', {'form': form, 'product': product})

# You would also typically add a delete view:
# def admin_product_delete(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('admin_product_list')
#     return render(request, 'admin/products/product_confirm_delete.html', {'product': product}) # You'll need a confirm delete template


@login_required
def customer_dashboard(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'customer/customer_dashboard.html', context)
    