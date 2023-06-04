from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Order, Customer, Product

User = get_user_model()


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
