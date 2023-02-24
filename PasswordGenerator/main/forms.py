from django import forms
from .models import Passwords


class CreateNew(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ["username", "email", "siteurl", "password"]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                    # "style": "width:500px",
                    "style": "height:30px",
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email ID",
                    # "style": "width:500px",
                    "style": "height:30px",
                    "class": "form-control",
                }
            ),
            "siteurl": forms.URLInput(
                attrs={
                    "placeholder": "Site URL",
                    # "style": "width:500px",
                    "style": "height:30px",
                    "class": "form-control",
                }
            ),
            "password": forms.TextInput(
                attrs={
                    "placeholder": "Password",
                    # "style": "width:500px",
                    "style": "height:30px",
                    "class": "form-control",
                    "required": "Flase",
                }
            )
        }
