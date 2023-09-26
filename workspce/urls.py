from django.urls import path, include
from . import views




app_name = 'workspace'
urlpatterns = [
    path('workspace-create/', views.WorkspaceCreateApiView.as_view(), name='workspace-create'),
    path('', views.WorkspaceListApiView.as_view(), name='workspace_list'),
    path('workspace/<pk>/', views.WorkspaceEditApiView.as_view(), name='workspace_edit'),
    path('workspace-delete/<int:pk>/', views.WorkspaceDeleteApiView.as_view(), name='workspace_edit'),

    
]
