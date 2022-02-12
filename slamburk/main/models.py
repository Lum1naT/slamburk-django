from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


GENDER_CHOICES = (
    ('F', _('Female')),
    ('M', _('Male')),
    ('U', _('Undefined')),
)
