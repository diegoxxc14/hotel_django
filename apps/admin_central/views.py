from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.reservas.models import Reservacion

# Create your views here.
def inicio(request):
    return render(request, 'index.html')   

@login_required
def admin_panel(request, template_name='inicio_admin.html'):
    res = Reservacion.objects.count()
    return render(request, template_name, {'nro_reservas':res})

