from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateModel(models.Model):
    create_at = models.DateTimeField(_('create'), auto_now_add=True)


    class Meta:
        abstract = True