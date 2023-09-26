from django.contrib import admin
from .models import  LinkSciol


# @admin.register(CardModel)
# class CardsAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address', 'workspce', 'create_at', 'is_active', 'id')
#     list_editable = ('is_active', )
#     list_filter = ('is_active', 'create_at')


# @admin.register(ResolotionSciolModel)
# class CardHomeAdmin(admin.ModelAdmin):
#     list_display = ('scial_name', 'format', 'create_at', 'id')
#     list_filter = ('create_at',)
    
@admin.register(LinkSciol)
class CardHomeAdmin(admin.ModelAdmin):
    list_display = ('sciol_name', 'id')