from django.contrib import admin
from django.utils.translation import gettext as _

from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name")
    verbose_name = _("User")
    verbose_name_plural = _("Users")
