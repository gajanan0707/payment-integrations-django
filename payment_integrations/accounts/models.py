from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    first_name = models.CharField(_('first name'), max_length=250, blank=True)
    last_name = models.CharField(_('last name'), max_length=250, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    user_name = models.CharField(
        max_length=500,
        help_text=_('Unique to Identify the user in the system'),
        unique=True,
    )
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('abstract_user')
        verbose_name_plural = _('abstract_users')
        # abstract = True

    def get_short_name(self):
        return self.first_name
