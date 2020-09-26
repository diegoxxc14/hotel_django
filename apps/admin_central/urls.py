from django.urls import path
from . import views

urlpatterns = [
    #Inicio de la página
    path('', views.inicio, name='inicio'),
    path('galeria', views.galeria, name='galeria'),

    #Inicio de la Administración
    path('control_panel/', views.control_panel, name='control_panel'),
]