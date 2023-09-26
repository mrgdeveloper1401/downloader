from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('create-link/', views.DownloadLinkAPIView.as_view()),
    path('delete-link/<pk>/', views.deleteLinkApiView.as_view()),
    
]
