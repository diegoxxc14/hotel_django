from django.shortcuts import render, redirect
from django.db.models import Sum
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from apps.reservas.models import Reservacion, Habitacion, Servicio, Periodo, Cliente
from django.contrib.auth.models import User
from .forms import CrearUserForm, EditarUserForm, EditarAvanzadoUserForm, CrearReservacionForm, CrearClienteForm, CrearPeriodoForm
from datetime import datetime, timedelta, date
import json

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CrearUsuario(CreateView):
    model = User
    form_class = CrearUserForm
    template_name_suffix = '_crear'
    success_url = reverse_lazy('home_admin:listar_users')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Usuario editado correctamente.')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditarUsuarioAvanzado(UpdateView):
    model = User
    form_class = EditarAvanzadoUserForm
    template_name_suffix = '_editar'
    success_url = reverse_lazy('home_admin:listar_users')
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Usuario editado correctamente.')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditarUsuarioBasico(UpdateView):
    model = User
    form_class = EditarUserForm
    template_name_suffix = '_editar'
    success_url = reverse_lazy('home_admin:listar_users')
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Usuario editado correctamente.')
        return super().form_valid(form)

@login_required
def listar_users(request, template_name='auth/listar_usuarios.html'):
    usuarios = User.objects.all()
    return render(request, template_name, {'usuarios':usuarios})

def inicio(request):
    habitaciones = Habitacion.objects.filter(activa=True).order_by('?')[:4]
    contexto = {
        'habitaciones':habitaciones,
    }
    return render(request, 'index.html', contexto)

def galeria(request):
    #obtener datos que serán enviados a la vista
    return render(request, 'gallery.html') 

def nuestro_hotel(request):
    #obtener datos que serán enviados a la vista
    return render(request, 'about.html') 

def contacto(request):
    #obtener datos que serán enviados a la vista
    return render(request, 'contact.html') 

@login_required
def control_panel(request, template_name='inicio_admin.html'):
    res = Reservacion.objects.count()
    total_pagos = Reservacion.objects.filter(estado='FN').aggregate(Sum('pago_total'))
    clientes_estancia = Reservacion.objects.filter(estado='EE').aggregate(Sum('nro_personas'))
    
    #Total de reservaciones según su estado
    por_confirmar = Reservacion.objects.filter(estado='PC').count()
    confirmadas = Reservacion.objects.filter(estado='CF').count()
    en_estadia = Reservacion.objects.filter(estado='EE').count()
    contexto = {
        'nro_reservas':res, 'total':total_pagos['pago_total__sum'],
        'nro_clientes':clientes_estancia['nro_personas__sum'], 'por_confirmar':por_confirmar,
        'confirmadas':confirmadas, 'en_estadia':en_estadia
    }
    return render(request, template_name, contexto)

def obtener_habs_disponibles(fi, fs):
    habitaciones = list()
    habs_act = Habitacion.objects.filter(activa=True)
    for hab in habs_act:
        res_hab = hab.habitaciones.all().order_by('periodo')  
        print('** Habitación: {0}'.format(hab))
        print('** Fecha Ingreso: {0}'.format(fi.date()))
        print('** Fecha Salida: {0}'.format(fs.date()))
        #Si todas las reservas son Canceladas y Finalizadas, la habitación está libre 
        if res_hab.filter(estado__in=['FN','CC']).count() == res_hab.count(): 
            print('==== Habitación Válida: {0}\n'.format(hab))
            habitaciones.append(hab)
        else:
            for res in res_hab: #Veficar cada Reservación de esa Habitación
                print('**** Reserva: {0}'.format(res.periodo))
                print('**** Estado: {0}'.format(res.estado))
                if res.periodo.fecha_ingreso <= fi.date() < res.periodo.fecha_salida or res.periodo.fecha_ingreso < fs.date() <= res.periodo.fecha_salida:            
                    if res.estado not in ['FN','CC']:
                        break
                    continue
                else:
                    if res.estado in ['FN','CC']:
                        continue
                    print('==== Habitación Válida: {0}\n'.format(hab))
                    habitaciones.append(hab)
                    break
    return habitaciones

@csrf_exempt
def elegir_habitaciones(request, template_name='admin_central/elegir_habitaciones.html'):
    fi = datetime.today()
    fs = fi + timedelta(days=1)
    
    #Obtener Servicios activos
    servicios = Servicio.objects.filter(activo=True)
    
    #Obtener las habitaciones disponibles en estas fechas
    habitaciones = obtener_habs_disponibles(fi, fs)

    fechaIngreso = fi
    fechaSalida = fs
    nroDias = 1
    nroHuespedes = 1

    #Habitaciones que se presentan en imágenes
    habs4 = Habitacion.objects.filter(activa=True).order_by('?')[:4]

    contexto = {
        'servicios':servicios, 'habitaciones':habitaciones,
        'fecIngreso':fechaIngreso, 'fecSalida':fechaSalida,
        'nroDias': nroDias, 'nroHuespedes':nroHuespedes, 'habs4':habs4
    }
    return render(request, template_name, contexto)

@csrf_exempt
def buscar_habitaciones(request, template_name='admin_central/elegir_habitaciones.html'):
    formato = '%m/%d/%Y'
    fi = datetime.strptime(request.POST.get(
        'fecha_ingreso', date.today().strftime(formato)), formato)
    fs = datetime.strptime(request.POST.get(
        'fecha_salida', (date.today() + timedelta(days=1)).strftime(formato)), formato)
    nroDias = int(request.POST.get('nro_dias', 1))
    nroHuespedes = int(request.POST.get('nro_huespedes', 1))
    
    #Obtener Servicios activos
    servicios = Servicio.objects.filter(activo=True)

    #Obtener las habitaciones disponibles en estas fechas
    habitaciones = obtener_habs_disponibles(fi, fs)
 
    #Habitaciones que se presentan en imágenes
    habs4 = Habitacion.objects.filter(activa=True).order_by('?')[:4]

    contexto = {
        'servicios':servicios, 'habitaciones':habitaciones,
        'fecIngreso':fi, 'fecSalida':fs,
        'nroDias': nroDias, 'nroHuespedes':nroHuespedes, 'habs4':habs4
    }
    return render(request, template_name, contexto)

@csrf_exempt
def pre_reservar(request, template_name='admin_central/crear_reservacion.html'):
    formato = '%m/%d/%Y'
    habitaciones_pks = json.loads(request.POST['habitaciones_pks'])
    print(habitaciones_pks)
    fechaIngreso = datetime.strptime(request.POST['fecha_ingreso'], formato)
    fechaSalida = datetime.strptime(request.POST['fecha_salida'], formato)
    nroDias = int(request.POST['nro_dias'])
    nroHuespedes = int(request.POST['nro_huespedes'])

    #Habitaciones a reservar
    habitaciones = Habitacion.objects.filter(pk__in=habitaciones_pks)

    #Calcular el total a pagar
    precioHab = Habitacion.objects.filter(pk__in=habitaciones_pks).aggregate(Sum('precio'))
    totalPagar = precioHab['precio__sum'] * nroDias * nroHuespedes

    formCliente = CrearClienteForm()

    formPeriodo = CrearPeriodoForm()
    formPeriodo.fields['fecha_ingreso'].initial = fechaIngreso
    formPeriodo.fields['fecha_salida'].initial = fechaSalida

    formReserva = CrearReservacionForm()
    formReserva.fields['nro_personas'].initial = nroHuespedes
    formReserva.fields['pago_total'].initial = totalPagar
    formReserva.fields['habitacion'].initial = habitaciones #Va oculto

    contexto = {
        'nro_dias':nroDias, 'form_reserva':formReserva, 'habitaciones':habitaciones,
        'form_cliente':formCliente, 'form_periodo':formPeriodo
    }
    return render(request, template_name, contexto)

@csrf_exempt
def crear_reservacion(request):
    print(request.POST)
    formato = '%d/%m/%Y' #Formato como llega desde el Fronted
    
    #Guardar Cliente
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    telefono = request.POST['telefono']
    email = request.POST['email']
    cliente = Cliente(nombres=nombres, apellidos=apellidos, telefono=telefono, email=email)
    cliente.save()

    #Guardar Periodo
    fechaIngreso = datetime.strptime(request.POST['fecha_ingreso'], formato)
    fechaSalida = datetime.strptime(request.POST['fecha_salida'], formato)
    periodo = Periodo(fecha_ingreso=fechaIngreso, fecha_salida=fechaSalida)
    periodo.save()

    #Obtener Habitaciones
    habitaciones_pks = dict(request.POST)['habitacion'] #values = request.POST.getlist('key')
    habitaciones = Habitacion.objects.filter(pk__in=habitaciones_pks)
    
    #Obtener Servicios activos
    servicios = Servicio.objects.filter(activo=True)

    #Guardar Reservacion
    nroHuespedes = int(request.POST['nro_personas'])
    pagoTotal = Decimal(request.POST['pago_total'])
    horaLlegada = request.POST['hora_llegada']
    petAdicional = request.POST['peticion_adicional']
    reservacion = Reservacion(nro_personas=nroHuespedes, pago_total=pagoTotal, 
        hora_llegada=horaLlegada, peticion_adicional=petAdicional,
        cliente=cliente, periodo=periodo)
    reservacion.save()
    reservacion.servicios.add(*servicios) #Asignar una lista de servicios a la reservacion
    reservacion.habitacion.add(*habitaciones) #Asignar una lista de habitaciones a la reservacion
    reservacion.save()

    messages.add_message(request, messages.SUCCESS, 'Su reservación se ha registrado con éxito. Uno de nuestros empleados se contactará contigo en breves instantes.')
    return redirect('home:elegir_hab')