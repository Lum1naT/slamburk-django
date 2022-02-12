from django import forms
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext as _

from .models import CREW_CHOICES, Crew


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

    def _get_all_active_crews():
        try:
            query = Crew.objects.filter(active=True)
            result = []
            for crew in query:
                result.append((crew.name[0:1], crew))
            return query
        except Crew.DoesNotExist:
            return False
    name = forms.CharField(label=_('Name'), widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "nameInput"}))
    crew = forms.ModelMultipleChoiceField(label=_('Crew'), queryset=_get_all_active_crews(), widget=forms.RadioSelect(
        attrs={"id": "crewInput"}))
