from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'user', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_id', 'user__username', 'email', 'user__first_name', 'user__last_name')
    ordering = ('customer_id',)
    readonly_fields = ('customer_id', 'created_at')
