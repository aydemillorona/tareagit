from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaprincipal, name='paginaprincipal'),
    path('futbol', views.futbol, name='futbol'),
    path('volley', views.volley, name='volley'),
    path('futsal', views.futsal, name='futsal'),
    path('sincontrincante', views.sincontrincante, name='sincontrincante'),
]