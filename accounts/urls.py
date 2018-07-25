from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('trial/', views.clean, name = 'trial'),

#    path('/accounts/trial/login', views.login, name = 'trial-login'),
#    path('/accounts/trial/create', views.signup, name = 'trial-create'),

]
