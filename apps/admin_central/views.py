from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from apps.reservas.models import Reservacion

# Create your views here.
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

