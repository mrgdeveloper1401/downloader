from django.contrib import admin
from .models import  LinkSciol

@admin.register(LinkSciol)
class CardHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_sciol', 'create_at')