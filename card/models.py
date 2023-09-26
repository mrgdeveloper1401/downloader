from django.db import models
from django.utils.translation import gettext_lazy as _
from workspce.models import WorkspaceModel, HomeModel
from accounts.models import User
from core.models import CreateModel


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
        
        

# new app
class CardHomeModel(CreateModel):
    scial_name = models.ForeignKey(HomeModel, on_delete=models.CASCADE)
    choose_format = (
        ('148', '148'),
        ('240', '240'),
        ('360', '360'),
        ('720', '720'),
        ('1080', '1080'))
    format = models.CharField(_('resolution'), max_length=4, choices=choose_format)
    
    class Meta:
        verbose_name = 'card_home'
        verbose_name_plural = 'card_homes'
        db_table = 'card'
        