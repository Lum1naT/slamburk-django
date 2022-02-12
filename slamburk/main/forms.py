from django import forms
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext as _

from .models import CREW_CHOICES


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
    name = forms.CharField(label=_('Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "nameInput"}))
    crew = forms.ChoiceField(label=_('Crew'), choices=CREW_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', "id": "crewInput"}))
