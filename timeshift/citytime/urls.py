# ice_cream/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
]
