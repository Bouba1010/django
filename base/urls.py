from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='accueil'),
    path('room/<str:pk>/', views.room,name='salon'),
    path('create-room/', views.createRoom,name='create'),
]
