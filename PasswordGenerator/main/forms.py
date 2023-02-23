from django import forms


class CreateNew(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;','class':'form-control'}), max_length=100, required=True,)
        email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}),required=False)
        siteurl = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Site URL', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
        password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}), max_length=100, required=False)
        

