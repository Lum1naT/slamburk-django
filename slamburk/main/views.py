from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm, LoginForm, CreateKnightForm, EditKnightForm
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


def _get_knight_by_id(id):
    try:
        result = Knight.objects.get(id=id)
        if result:
            return result
    except Knight.DoesNotExist:
        return False


def _get_crew_by_name(name):
    try:
        result = Crew.objects.get(name=name)
        if result:
            return result
    except Crew.DoesNotExist:
        return False


def _get_all_active_crews():
    try:
        query = Crew.objects.filter(active=True)
        for q in query:
            print(str((q)))
        return query
    except Crew.DoesNotExist:
        return False


def _get_crew_capacity():
    all_crews = _get_all_active_crews()
    result = []
    for crew in all_crews:
        count = _count_knights_in_crew(crew)
        result.append((str(crew), str(count), str(
            crew.capacity), str(crew.upload)))
    print(str(result))
    return result


def _count_knights_in_crew(crew):
    try:
        result = Knight.objects.filter(crew=crew).count()
        if result is None:
            return 0
        else:
            return result
    except Knight.DoesNotExist:
        return False


def _get_all_knights_for_user(user):
    try:
        result = Knight.objects.filter(user=user)
        if result:
            return result
    except Knight.DoesNotExist:
        return False


def _knight_dict_from_knight(knight):
    result = {
        "first_name": knight.first_name,
        "last_name": knight.last_name,
        "crew": str(knight.crew),
    }
    print(result)
    return result


def _create_new_user(email, password, name=None):
    new_user = User()
    new_user.email = email
    new_user.password = password
    if name:
        new_user.name = name
    new_user.save()
    return new_user


def _create_new_knight(first_name, last_name, crew, user):
    new_knight = Knight()
    new_knight.first_name = first_name
    new_knight.last_name = last_name
    new_knight.crew = crew
    new_knight.user = user
    new_knight.save()
    return new_knight


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
        crew_capacities = _get_crew_capacity()
        return render(request, 'main/create_knight.html', {"form": form, "crewcap": crew_capacities})


def edit_knight(request, id):
    if request.method == "GET":
        if request.session["user_id"] is not None:
            user = _get_user_by_id(request.session["user_id"])
            knight = _get_knight_by_id(id)

            if isinstance(knight, bool):
                print("Knight with id: " + str(id) + " not found")
                pass
                return redirect("all_knights_overview")
            else:
                if knight.user.id != user.id:
                    return redirect("all_knights_overview")
                form_data = _knight_dict_from_knight(knight)
            form = EditKnightForm(initial=form_data)
            crew_capacities = _get_crew_capacity()
            return render(request, 'main/edit_knight.html', {"form": form, "crewcap": crew_capacities})


def process_create_knight(request):
    if request.method == "POST":
        if request.session["user_id"] is not None:
            user = _get_user_by_id(request.session["user_id"])
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            crew = request.POST.get('crew', '')
            found_crew = _get_crew_by_name(crew)
            if isinstance(found_crew, bool):
                # Error, Crew not found
                return redirect("create_knight")
            else:
                capacity = found_crew.capacity
                taken = _count_knights_in_crew(found_crew)
                if capacity > taken:
                    # OK
                    new_knight = _create_new_knight(
                        first_name, last_name, found_crew, user)
                    if new_knight:
                        print(str(new_knight.id))
                        return redirect("all_knights_overview")
                elif capacity <= taken:
                    # Crew Full
                    return redirect("create_knight")
                return redirect("create_knight")

def


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
