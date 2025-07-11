from django.contrib import admin
from .models import Category, Product, Order, OrderItem

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'total_amount', 'is_completed')
    list_filter = ('is_completed', 'order_date')
    search_fields = ('customer__user__first_name', 'customer__user__last_name', 'customer__email')
    ordering = ('-order_date',)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_order')
    search_fields = ('order__id', 'product__name')
    list_filter = ('product',)
