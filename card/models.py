from django.db import models
from django.utils.translation import gettext_lazy as _
from workspce.models import WorkspaceModel
from accounts.models import User


class CardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ucard')
    workspce = models.ForeignKey(WorkspaceModel, on_delete=models.CASCADE, related_name='Wcard')
    address = models.CharField(_('link address'),max_length=255)
    create_at = models.DateTimeField(_('create url'), auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.address[:30]
    
    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        db_table = 'card-model'