from django.forms import ModelForm, TextInput, PasswordInput
from .models import Account


class UserLogin(ModelForm):
    class Meta:
        model = Account
        fields = ["email", "password"]
        widget = {
            'email': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }


class UserRegistration(ModelForm):
    class Meta:
        model = Account
        fields = ["email", "password"]
        widget = {
            'email': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'type': 'password'}),

        }
