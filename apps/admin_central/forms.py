from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.reservas.models import Reservacion, Cliente, Periodo
  
class CrearUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']

class EditarAvanzadoUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True})
        }

class EditarUserForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True})
        }

class CrearClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CrearPeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'readonly': True}),
            'fecha_salida': forms.DateInput(attrs={'readonly': True})
        }

class CrearReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['nro_personas', 'pago_total', 'hora_llegada',
                'peticion_adicional', 'habitacion']
        widgets = {
            'nro_personas': forms.NumberInput(attrs={'readonly': True}),
            'pago_total': forms.NumberInput(attrs={'readonly': True}),
            'peticion_adicional': forms.Textarea(attrs={'rows' : 3, 'style':'resize:none;'}),
            'hora_llegada': forms.TimeInput(attrs={'type': 'time'})
        }