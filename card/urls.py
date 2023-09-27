from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('create-link/', views.InstagramDownloadView.as_view()),
    path('show-link/', views.ShowLinkApiView.as_view()),
    path('delete-link/<pk>/', views.deleteLinkApiView.as_view()),
    
]
