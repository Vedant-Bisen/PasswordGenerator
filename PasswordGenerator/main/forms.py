from django import forms
from .models import Passwords


class CreateNew(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ["username", "email", "siteurl", "password"]

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email ID","class": "form-control"}),
            "siteurl": forms.URLInput(attrs={"placeholder": "Site URL","class": "form-control"}),
            "password": forms.TextInput(attrs={"placeholder": "Password","class": "form-control"}),
        }
