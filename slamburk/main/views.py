from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm, LoginForm, CreateKnightForm
from .models import User, Knight, Crew
## Helpers, Methods ##


def _get_user_by_email(email):
    try:
        result = User.objects.get(email=email)
        if result:
            return result
    except User.DoesNotExist:
        return False


def _get_user_by_id(id):
    try:
        result = User.objects.get(id=id)
        if result:
            return result
    except User.DoesNotExist:
        return False


def _get_all_knights_for_user(user):
    try:
        result = Knight.objects.filter(user=user)
        if result:
            return result
    except Knight.DoesNotExist:
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


def account_logout(request):
    if request.method == "GET":
        if request.session["user_id"] is not None:
            del request.session["user_id"]
            return redirect("account_login")


def account_overview(request):
    if request.method == "GET":
        if request.session["user_id"] is not None:
            # TODO: ADD FORM!
            return render(request, "main/account_personal.html")
        else:
            return redirect("account_login")


def all_knights_overview(request):
    if request.method == "GET":
        if request.session["user_id"] is not None:
            print("ok: " + str(request.session["user_id"]))
            user = _get_user_by_id(request.session["user_id"])
            all_knights = _get_all_knights_for_user(user)
            print(str(all_knights))
            return render(request, "main/user_knights_overview.html", {"knights": all_knights})
        else:
            return redirect("account_login")


def create_knight(request):
    if request.method == "GET":
        form = CreateKnightForm()
        return render(request, 'main/create_knight.html', {"form": form})


def process_create_knight(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        crew = request.POST.get('crew', '')
        # TODO: LINK USER!
        return render(request, 'main/create_knight.html', {"form": "form"})


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
        user = _get_user_by_email(email)
        if isinstance(user, bool):
            # user not found, Error
            return redirect("account_login")
        else:
            # user found, OK.
            request.session["user_id"] = user.id
            request.session["user_email"] = user.email

            if check_password(password, user.password):
                # password ok.
                redirect("all_knights_overview")
            else:
                # password not ok
                redirect()
            return redirect("all_knights_overview")
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
            return redirect("account_login")
        else:
            # user found, Error
            return redirect("account_register")

        return redirect("account_register")
