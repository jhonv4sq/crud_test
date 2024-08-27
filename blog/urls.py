from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('create/', views.create, name='posts_create'),
]