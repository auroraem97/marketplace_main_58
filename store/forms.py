from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']