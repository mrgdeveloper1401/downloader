from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('create/', views.UserCreateApiView.as_view()),
    path('profile/<pk>/', views.ProfileApiview.as_view()),

]
