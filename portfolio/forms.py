from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "field"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "class": "field"}),
            "message": forms.Textarea(
                attrs={"placeholder": "What would you like to build?", "class": "field", "rows": 5}
            ),
        }
