from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = [
    url('add_user/', views.add_user, name='add_user'),
    url('edit_user/', views.edit_user, name='edit_user'),
    url('delete_user/', views.delete_user, name='delete_user'),
    url('list_user/', views.list_user, name='list_user'),
]