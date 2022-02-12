from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password

from .forms import RegisterForm, LoginForm
from .models import User
## Helpers, Methods ##


def _get_user_by_email(email):
    try:
        result = User.objects.get(email=email)
        if result:
            return result
    except User.DoesNotExist:
        return False


def _create_new_user(email, password, name=None):
    new_user = User()
    new_user.email = email
    new_user.password = password
    if name:
        new_user.name = name
    new_user.save()
    return new_user


## Views ##
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
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        return redirect("account_login")


def process_account_register(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        password_check = request.POST.get('password_check', '')
        if password != password_check:
            # passwords dont match
            return redirect("account_register")
        user = _get_user_by_email(email)
        if isinstance(user, bool):
            # user not found, OK
            hashed_password = make_password(password)
            new_user = _create_new_user(
                email=email, name=name, password=hashed_password)
            print("OK.")
            return redirect("account_register")
        else:
            # user found, Error
            return redirect("account_register")

        return redirect("account_register")
