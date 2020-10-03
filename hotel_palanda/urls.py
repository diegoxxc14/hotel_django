"""hotel_palanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #Inicio del Sitio Web
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),#Test
    path('', include(('apps.admin_central.urls', 'admin_central'), namespace='home')),
    
    #Aplicación admin_central
    path('admin_central/', include(('apps.admin_central.urls', 'admin_central'), namespace='home_admin')),
    #Aplicación reservas
    path('reservas/', include(('apps.reservas.urls', 'reservas'), namespace='reservas')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)