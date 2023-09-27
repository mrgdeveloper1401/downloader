from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('create-link-instagram/', views.InstagramDownloadView.as_view()),
    path('create-link-twitter/', views.TwitterDownloadView.as_view()),
    path('create-link-facebook/', views.FacebookDownloadView.as_view()),
    path('show-all-link/', views.ShowLinkApiView.as_view()),
    path('delete-link/<pk>/', views.deleteLinkApiView.as_view()),
    
]
