from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.weather_api, name='weather_api'),
]
