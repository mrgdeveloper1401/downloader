from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('create-link/', views.LinkListApiView.as_view()),
    path('delete-link/<pk>/', views.DestroyAPIView.as_view()),
    
]
