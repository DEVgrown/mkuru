from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Add the 'role' field and other fields you added in the form
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('cashier', 'Cashier'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    # Add the fields you added in the form to the model
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # Email is already in AbstractUser, but ensure it's handled correctly if you
    # want to make it unique or the primary identifier
    # email = models.EmailField(unique=True) # Example if you want unique emails
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)


    # Add unique related_name values for the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set', # Change related_name here
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_user_set', # Change related_name here
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username
