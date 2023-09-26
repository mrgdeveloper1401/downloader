from django.urls import path, include
from . import views




app_name = 'card'
urlpatterns = [
    path('lc_card/', views.LinkSciolListCreateApiView.as_view()),
    
]
