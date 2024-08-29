from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('post/create', views.create, name='posts_create'),
    path('post/store', views.store, name='posts_store'),
    path('post/<int:id>', views.show, name='posts_show'),
    path('post/<int:id>/delete', views.destroy, name='posts_delete'),
    path('post/<int:id>/edit', views.edit, name='posts_edit'),
    path('post/<int:id>/update', views.update, name='posts_update'),
]