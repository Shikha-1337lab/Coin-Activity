from .views import CoinRudView, CoinAPIView
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('<int:pk>/', CoinRudView.as_view(), name='post-rud'),
    path('', CoinAPIView.as_view(), name='post-listcreate'),
    path('createAll', views.insertDB, name='post-create'),
    path('all/limit=<int:limit>', views.api_all, name='post-all'),

]
