from django import forms

class CreateNew(forms.Form):
    username = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email",required=False)
    siteurl = forms.URLField(label="Site URL", required=True)
    password = forms.CharField(label="Password", max_length=100, required=False)
    