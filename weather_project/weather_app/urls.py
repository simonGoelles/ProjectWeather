from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.data_to_model, name='data_to_model'),
    path('plz/', views.plz, name='plz'),
    path('plz/send/', views.weather_api, name='weather_api'),
    path('plz/login/', views.login, name='login'),
    path('plz/login/send/', views.login_search, name='login_search'),
    path('plz/login/register.html', views.register, name='register'),
    path('plz/login/register.html/send/', views.register_add, name='register_add'),
]
