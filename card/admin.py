from django.contrib import admin
from .models import CardModel, CardHomeModel


# @admin.register(CardModel)
# class CardsAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address', 'workspce', 'create_at', 'is_active', 'id')
#     list_editable = ('is_active', )
#     list_filter = ('is_active', 'create_at')


@admin.register(CardHomeModel)
class CardHomeAdmin(admin.ModelAdmin):
    list_display = ('scial_name', 'format', 'create_at')
    list_filter = ('create_at',)