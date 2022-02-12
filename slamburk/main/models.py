from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


# Create your models here.


GENDER_CHOICES = (
    ('F', _('Female')),
    ('M', _('Male')),
    ('U', _('Undefined')),
)


STATUS_CHOICES = (
    ('U', _('Unverified')),
    ('V', _('Verified')),
    ('R', _('Restricted')),
)


class User(models.Model):
    email = models.EmailField(_("Email"), unique=True)
    name = models.CharField(_("Name"), max_length=100,
                            null=True, blank=True, default=None)
    password = models.CharField(_("Password"),
                                max_length=1024, null=True, blank=True, default=None)
    status = models.CharField(
        _("Status"), max_length=10, choices=STATUS_CHOICES, default="U")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
