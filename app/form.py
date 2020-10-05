from django import forms
from django.forms import ModelForm
from .models import Contact
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'