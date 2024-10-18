from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('outsiders/', views.outsiders, name='outsiders'),
    path('id_detection/', views.id_detection, name = 'IDdetection'),
    path('video_feed/<int:camera_id>/', views.video_feed, name='video_feed'),
]