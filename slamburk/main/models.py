from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


# Create your models here.


GENDER_CHOICES = (
    ('F', _('Female')),
    ('M', _('Male')),
    ('U', _('Undefined')),
)


USER_STATUS_CHOICES = (
    ('U', _('Unverified')),
    ('V', _('Verified')),
    ('R', _('Restricted')),
)

KNIGHT_STATUS_CHOICES = (
    ('A', _('Active')),
    ('I', _('Inactive')),
    ('C', _('Cancelled')),
)
CREW_CHOICES = (
    ('R', _('Rožmberkové')),
    ('I', _('IDK')),
    ('C', _('Co já vím')),
)


class User(models.Model):
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First Name"), max_length=100,
                            null=True, blank=True, default=None)
    last_name = models.CharField(_("Last Name"), max_length=100,
                            null=True, blank=True, default=None)
    password = models.CharField(_("Password"),
                                max_length=1024, null=True, blank=True, default=None)
    status = models.CharField(
        _("Status"), max_length=10, choices=USER_STATUS_CHOICES, default="U")

    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Crew(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    capacity = models.IntegerField(_("Capacity"), default=30)
    active = models.BooleanField(_("Active"), default=True)
    upload = models.ImageField(_("Crest"),
                               upload_to='uploads/', blank=True, null=True, default=None)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Crew, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Knight(models.Model):
    first_name = models.CharField(
        _("First Name"), max_length=100, unique=False)
    last_name = models.CharField(_("Last Name"), max_length=100, unique=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    crew = models.ForeignKey(
        Crew, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(
        _("Status"), max_length=10, choices=KNIGHT_STATUS_CHOICES, default="A")

    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Knight, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name
