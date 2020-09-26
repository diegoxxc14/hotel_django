from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from apps.reservas.models import Reservacion
from django.contrib.auth.models import User
from .forms import CrearUserForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CrearUsuario(CreateView):
    model = User
    form_class = CrearUserForm
    template_name_suffix = '_crear'
    success_url = reverse_lazy('reservas:listar_hab')

def inicio(request):
    #obtener datos que serán enviados a la vista
    return render(request, 'index.html')

def galeria(request):
    #obtener datos que serán enviados a la vista
    return render(request, 'gallery.html') 

@login_required
def control_panel(request, template_name='inicio_admin.html'):
    res = Reservacion.objects.count()
    total_pagos = Reservacion.objects.filter(estado='FN').aggregate(Sum('pago_total'))
    return render(request, template_name, {'nro_reservas':res, 'total':total_pagos['pago_total__sum']})

