from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('outsiders/', views.outsiders, name='outsiders'),
    path('Id-detection/', views.id_detection, name = 'IDdetection'),
]