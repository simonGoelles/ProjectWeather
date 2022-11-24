from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.weather_api, name='weather_api'),
    path('login/', views.login, name='login'),
    path('login/send/', views.login_search, name='login_search'),
    path('login/register.html', views.register, name='register'),
    path('login/register.html/send/', views.register_add, name='register_add'),
]
