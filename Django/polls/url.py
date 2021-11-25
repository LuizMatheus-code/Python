from django.urls import path

from . import views

url_patter = [
    path('', views.index, name='index')
]