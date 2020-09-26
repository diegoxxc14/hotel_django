from django.urls import path
from . import views

urlpatterns = [
    path('listar_reservas/', views.listar_reservas, name='listar_res'),
    path('gestionar_reserva/<pk>', views.GestionarReservacion.as_view(), name='gestionar_res'),
    
    #path('crear_habitacion/', views.crear_habitacion, name='crear_hab'),
    path('crear_habitacion/', views.CrearHabitacion.as_view(), name='crear_hab'),
    path('editar_habitacion/<pk>', views.EditarHabitacion.as_view(), name='editar_hab'),
    path('listar_habitaciones/', views.listar_habitaciones, name='listar_hab'),
    #path('', views.admin_panel, name='admin_panel'),

    path('crear_dethabitacion/', views.CrearDetalleHabitacion.as_view(), name='crear_detHab'),
    path('listar_dethabitacion/', views.listar_detallesHab, name='listar_detHab'),

    path('crear_servicio/', views.CrearServicio.as_view(), name='crear_ser'),
    path('listar_servicios/', views.listar_servicios, name='listar_ser'),
]