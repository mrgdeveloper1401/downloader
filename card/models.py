from django.db import models
from django.utils.translation import gettext_lazy as _

class LinkSciol(models.Model):
    link_sciol = models.URLField(_('link'), max_length=255)
    create_at = models.DateTimeField(_('create link'), auto_now_add=True)


    class Meta:
        verbose_name = 'LinkSciol'
        verbose_name_plural = 'LinkSciols'
        db_table = 'LinkSciol'
        
