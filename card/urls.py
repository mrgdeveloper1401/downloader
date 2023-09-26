from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('list-link/', views.LinkSciolListCreateApiView.as_view()),
    path('create-link/', views.LinkCreateApiView.as_view()),
    path('delete-link/<pk>/', views.LinkSciolDelete.as_view()),
    
]
