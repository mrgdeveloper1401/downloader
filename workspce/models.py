from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class WorkspaceModel(models.Model):
    workspace_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='wuser')
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(_('create workspace'), auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'wprkspace'
        verbose_name_plural = 'workspaces'
        db_table = 'workspace_model'