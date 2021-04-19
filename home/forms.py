from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Ticket, Review, Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre",
            "description": "Description"
        }
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
        labels = {
            "rating": "Note",
            "headline": "Titre",
            "body": "Commentaire",
        }

class UserLogin(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["email", "password"]



class UserSignup(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']

