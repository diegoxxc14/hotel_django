from django.urls import path
from . import views

urlpatterns = [
    #Inicio de la Administración
    path('', views.admin_panel, name='admin_panel'),
]