from django.db import models
from django.contrib.auth.models import User, Group, Permission
import uuid

class Customer(models.Model):
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    groups = models.ManyToManyField(Group, related_name='customer_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customer_permissions')
    customer_id = models.CharField(max_length=3, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.order_by('customer_id').last()
            if last_customer:
                next_id = int(last_customer.customer_id[2:]) + 1
            else:
                next_id = 1
            self.customer_id = f"CU{next_id:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"
