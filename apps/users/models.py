from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import UnicodeUsernameValidator


class User(AbstractUser):
    username = models.CharField(
        _('Username'), max_length=150, unique=True, validators=[UnicodeUsernameValidator()],
        help_text=_('Required. 150 characters or fewer. Letters, digits and ./+/-/_ only.'),
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
