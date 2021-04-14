from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
        labels = {
            "rating": "Note",
            "headline": "Titre",
            "body": "Commentaire",
        }
