from django import forms
from .models import Reservacion 
  
class ReservacionForm(forms.ModelForm): 
    class Meta:
        model = Reservacion
        fields = ['nro_personas', 'pago_total', 'hora_llegada',
                'peticion_adicional', 'estado']
        widgets = {
            'nro_personas': forms.NumberInput(attrs={'readonly': True}),
            'pago_total': forms.NumberInput(attrs={'readonly': True}),
            'hora_llegada': forms.TimeInput(format='%H:%M', attrs={'readonly': True}),
            #'cliente': forms.TextInput(attrs={'disabled': True}),
            #'periodo': forms.Select(attrs={'disabled': True}),
            'peticion_adicional': forms.Textarea(attrs={'readonly': True, 'rows' : 3, 'style':'resize:none;'}),
        }