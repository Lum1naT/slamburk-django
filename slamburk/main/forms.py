from django import forms
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext as _

from .models import CREW_CHOICES, Crew, Knight


def _get_all_active_crews():
    try:
        query = Crew.objects.filter(active=True)
        for q in query:
            print(str((q)))
        return query
    except Crew.DoesNotExist:
        return False


class RegisterForm(forms.Form):
    name = forms.CharField(label=_('Your name'), max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "nameInput"}))
    email = forms.EmailField(label=_('Your Email'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "emailInput"}))
    password = forms.CharField(label=_('Your Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', "id": "passwordInput"}))
    password_check = forms.CharField(label=_('Same password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', "id": "passwordCheckInput"}))


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Your Email'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "emailInput"}))
    password = forms.CharField(label=_('Your Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', "id": "passwordInput"}))


class CreateKnightForm(forms.Form):
    first_name = forms.CharField(label=_('First Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "firstnameInput", "placeholder": "Jméno"}))
    last_name = forms.CharField(label=_('Last Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "lastnameInput", "placeholder": "Příjmení"}))
    crew = forms.ModelMultipleChoiceField(label=_('Crew'), queryset=Knight.objects.none(), widget=forms.RadioSelect(
        attrs={"id": "crewInput"}))


class EditKnightForm(forms.Form):
    first_name = forms.CharField(label=_('First Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "firstnameInput", "placeholder": "Jméno"}))
    last_name = forms.CharField(label=_('Last Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "lastnameInput", "placeholder": "Příjmení"}))
    crew = forms.ModelChoiceField(label=_('Crew'), queryset=Knight.objects.none(), widget=forms.RadioSelect(
        attrs={"id": "crewInput"}))
