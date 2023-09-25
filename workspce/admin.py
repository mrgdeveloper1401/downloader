from django.contrib import admin
from .models import WorkspaceModel

@admin.register(WorkspaceModel)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'workspace_user', 'id', 'create_at', 'is_active')
    list_editable = ('is_active', )
    list_filter  = ('create_at', 'is_active')