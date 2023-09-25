from django.contrib import admin
from .models import CardModel


@admin.register(CardModel)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'workspce', 'create_at', 'is_active', 'id')
    list_editable = ('is_active', )
    list_filter = ('is_active', 'create_at')
