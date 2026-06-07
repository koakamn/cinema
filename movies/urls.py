from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),

]
