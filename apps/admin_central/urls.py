from django.urls import path
from . import views

urlpatterns = [
    #Inicio de la página
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria, name='galeria'),
    path('nuestro_hotel/', views.nuestro_hotel, name='nuestro_hotel'),
    path('contacto/', views.contacto, name='contacto'),

    path('elegir_habitaciones/', views.elegir_habitaciones, name='elegir_hab'),
    path('buscar_habitaciones/', views.buscar_habitaciones, name='buscar_hab'),
    path('reservacion_previa/', views.pre_reservar, name='pre_res'),
    path('crear_reservacion/', views.crear_reservacion, name='crear_res'),

    #Inicio de la Administración
    path('control_panel/', views.control_panel, name='control_panel'),

    path('crear_usuario/', views.CrearUsuario.as_view(), name='crear_user'),
    path('editar_usuario/user/<pk>', views.EditarUsuarioBasico.as_view(), name='editar_basico'),
    path('editar_usuario/admin/<pk>', views.EditarUsuarioAvanzado.as_view(), name='editar_avanzado'),
    path('listar_usuarios/', views.listar_users, name='listar_users'),
]