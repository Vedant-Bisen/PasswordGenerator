from django.shortcuts import render
from .models import Passwords
from .forms import CreateNew
from .generatorFile import generator

# Create your views here.

def home(response):
    return render(response, "main/base.html", {})


def new(response):
    if response.method == "POST":
        form = CreateNew(response.POST)
        if form.is_valid():
            n = form.cleaned_data["username"]
            e = form.cleaned_data["email"]
            if form.cleaned_data["password"] == "":
                p = generator()
            else:
                p = form.cleaned_data["password"]

            r = Passwords(username=n, email=e, password=p)
            r.save()
    else:
        form = CreateNew()
            
    return render(response, "main/new.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})
