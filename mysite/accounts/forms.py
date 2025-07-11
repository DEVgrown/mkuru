# mysite/accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group, User
from .models import Customer

class CustomerUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CustomerForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True)
    
    class Meta:
        model = Customer
        fields = ('email', 'phone_number', 'address')
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address', 'rows': 3}),
        }
