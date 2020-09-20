from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
@login_required
def listar_habitaciones(request, template_name='reservas/listar_habitaciones.html'):
    lista_habs = Habitacion.objects.all()
    return render(request, template_name, {'habitaciones':lista_habs})

@method_decorator(login_required, name='dispatch')
class CrearHabitacion(CreateView):
    model = Habitacion
    #fields = ['numero', 'tipo', 'precio', 'planta', 'activa', 'detalles']
    fields = '__all__'
    template_name_suffix = '_crear'
    success_url = reverse_lazy('reservas:listar_hab')

@method_decorator(login_required, name='dispatch')
class EditarHabitacion(UpdateView):
    model = Habitacion
    #fields = ['numero', 'tipo', 'precio', 'planta', 'activa', 'detalles']
    fields = '__all__'
    template_name_suffix = '_editar'
    success_url = reverse_lazy('reservas:listar_hab')