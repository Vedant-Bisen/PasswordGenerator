from django.shortcuts import render
from .models import Passwords

# Create your views here.

def home(response):
    return render(response, "main/base.html", {})

def generate(response):
    pass