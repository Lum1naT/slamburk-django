from django.contrib import admin
from django.utils.translation import gettext as _

from .models import User, Crew, Knight
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    readonly_fields = ("created_at", "modified_at")
    verbose_name = _("User")
    verbose_name_plural = _("Users")


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity")
    readonly_fields = ("created_at", "modified_at")
    verbose_name = _("Crew")
    verbose_name_plural = _("Crews")


@admin.register(Knight)
class KnightAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "crew", "created_at")
    readonly_fields = ("created_at", "modified_at")
    verbose_name = _("Knight")
    verbose_name_plural = _("Knights")
