from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at',)
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '+91 111 1234567', 'type': 'tel'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control'}),
            'Query': forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}),
        }
