from django import forms
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext as _

from .models import GENDER_CHOICES


class RegisterForm(forms.Form):
    name = forms.CharField(label=_('Your name'), max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "nameInput"}))
    surname = forms.CharField(label=_('Your surname'), max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "surnameInput"}))
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