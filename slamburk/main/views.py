from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'main/index.html')


def account_register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'main/account_register.html', {"form": form})


def account_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'main/account_login.html', {"form": form})


def process_account_login(request):
    if request.method == "POST":
        
        return redirect("account_login")
