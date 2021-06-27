from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile', 'company', 'designation', 'notes']
        widgets = {
            'notes': forms.Textarea(
                attrs={
                'rows': 3,
                }
            ),
        }
