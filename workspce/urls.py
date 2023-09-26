from django.urls import path, include
from . import views




app_name = 'workspace'
urlpatterns = [
    path('', views.SciolListCreateApiview.as_view()),
    
        
]
