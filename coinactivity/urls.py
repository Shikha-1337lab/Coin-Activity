from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from coins import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout/', views.logout, name = 'logout'),
    path('accounts/', include('accounts.urls')),
    # path('coins/', include('coins.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
