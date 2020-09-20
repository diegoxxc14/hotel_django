from django.urls import path
from . import views

urlpatterns = [
    #path('crear_habitacion/', views.crear_habitacion, name='crear_hab'),
    path('crear_habitacion/', views.CrearHabitacion.as_view(), name='crear_hab'),
    path('editar_habitacion/<pk>', views.EditarHabitacion.as_view(), name='editar_hab'),
    path('listar_habitaciones/', views.listar_habitaciones, name='listar_hab'),
    #path('', views.admin_panel, name='admin_panel'),
]