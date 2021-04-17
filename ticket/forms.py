from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre",
            "description": "Description"
        }
