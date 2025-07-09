from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    men_category = Category.objects.filter(name__iexact='Men').first()
    women_category = Category.objects.filter(name__iexact='Women').first()
    kids_category = Category.objects.filter(name__iexact='Kids').first()
    accessories_category = Category.objects.filter(name__iexact='Accessories').first()
    men_products = Product.objects.filter(category=men_category) if men_category else []
    women_products = Product.objects.filter(category=women_category) if women_category else []
    kids_products = Product.objects.filter(category=kids_category) if kids_category else []
    accessories_products = Product.objects.filter(category=accessories_category) if accessories_category else []
    # Set base template depending on authentication
    base_template = 'includes/base.html' if request.user.is_authenticated else 'includes/customer/base.html'
    context = {
        'products': products,
        'categories': categories,
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
        'accessories_products': accessories_products,
        'base_template': base_template,  # <-- This is required for your template to work!
    }
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
    categories = Category.objects.all()
    men_category = Category.objects.filter(name__iexact='Men').first()
    women_category = Category.objects.filter(name__iexact='Women').first()
    kids_category = Category.objects.filter(name__iexact='Kids').first()
    accessories_category = Category.objects.filter(name__iexact='Accessories').first()
    men_products = Product.objects.filter(category=men_category) if men_category else []
    women_products = Product.objects.filter(category=women_category) if women_category else []
    kids_products = Product.objects.filter(category=kids_category) if kids_category else []
    accessories_products = Product.objects.filter(category=accessories_category) if accessories_category else []
    context = {
        'products': products,
        'categories': categories,
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
        'accessories_products': accessories_products,
    }
    return render(request, 'includes/customer/customer_dashboard.html', context)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

from django.http import Http404

def single_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('Product not found')
    return render(request, 'shop/single-product.html', {'product': product})
    