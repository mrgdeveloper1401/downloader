from django.db import models
from django.utils.translation import gettext_lazy as _
# from accounts.models import User
from core.models import CreateModel

# class WorkspaceModel(models.Model):
#     workspace_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='wuser')
#     name = models.CharField(max_length=50)
#     create_at = models.DateTimeField(_('create workspace'), auto_now_add=True)
#     is_active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return f'{self.name}'
    
#     class Meta:
#         verbose_name = 'wprkspace'
#         verbose_name_plural = 'workspaces'
#         db_table = 'workspace_model'
        


# new ---------------------------------------------------------
class HomeModel(CreateModel):
    choose_sciol = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'Linkedin'),
    )
    choose = models.CharField(_('scoil'), choices=choose_sciol, max_length=9)
    
    def __str__(self):
        return self.choose
    
    class Meta:
        verbose_name = 'sciol name'
        verbose_name_plural = 'sciol names'
        db_table = 'sciol_name'
    