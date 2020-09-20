from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Periodo)
admin.site.register(Reservacion)
admin.site.register(Habitacion)
admin.site.register(ServicioIncluido)
admin.site.register(DetalleHabitacion)