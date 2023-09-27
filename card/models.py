from django.db import models
from django.utils.translation import gettext_lazy as _

class LinkSciol(models.Model):
    link_sciol = models.URLField(_('link'), max_length=255)


    class Meta:
        verbose_name = 'LinkSciol'
        verbose_name_plural = 'LinkSciols'
        db_table = 'LinkSciol'
        
