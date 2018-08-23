from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from coins import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('newsfeed_editor/', views.newsfeed_editor, name='newsfeed_editor'),
    path('market/', views.market, name='market'),
    path('logout/', views.logout, name = 'logout'),
    path('accounts/', include('accounts.urls')),
    path('api/coins/', include(('coins.api.urls','coins'), namespace='api-coins')),

#    path('coins/', include('coins.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
