from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from coins import views

urlpatterns = [
    path('newsfeed_editor', views.newsfeed_editor, name='newsfeed_editor'),

    ]
