from django.forms import ModelForm, TextInput, PasswordInput
from .models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLogin(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["email", "password"]



class UserSignup(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']

