from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel


class Language(CreateModel):
    choose_langguge = (
        ('english(uk)', 'English(UK)'),
        ('english(us)', 'English(US)'),
        ('persion', 'Persion'),
        ('arabic', 'Arabic'),
        ('Hindi', 'Hindi'),
        ('Turkish', 'Turkish')
    )
    
    languges = models.CharField(_('languge'), max_length=11, choices=choose_langguge)
    
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        db_table = 'Language'