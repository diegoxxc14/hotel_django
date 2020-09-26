from django.db import models

PLANTAS = [
    ('PB','Planta baja'),
    ('1ra','1er Piso'),
    ('2da','2do Piso'),
    ('3ra','3er Piso'),
]

ESTADO_RESERVACION = [
    ('PC','Por confirmar'),
    ('CF','Confirmada'),
    ('EE','En estadia'),
    ('FN','Finalizada'),
    ('CC','Cancelada'),
]

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.apellidos + ' ' + self.nombres

class DetalleHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    #foto = models.ImageField() #pip install Pillow
    numero = models.CharField(verbose_name='Número:', max_length=4, unique=True)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    planta = models.CharField(max_length=3, choices=PLANTAS)
    activa = models.BooleanField(default=True) #Controlar si aparecerá en las reservas
    detalles = models.ManyToManyField(DetalleHabitacion, related_name='detalles_habitacion')

    def __str__(self):
        return str(self.numero) + ' ' + self.tipo

class Periodo(models.Model):
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return 'Desde el {0} al {1}'.format(self.fecha_ingreso, self.fecha_salida)

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.TextField(max_length=100, blank=True)
    activo = models.BooleanField(default=True, null=False) #Controlar si el servicio está incluido o no

    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    nro_personas = models.IntegerField(help_text='Niños mayores de 12 años pagan tarifa completa', default=1)
    pago_total = models.DecimalField(max_digits=8, decimal_places=2)
    hora_llegada = models.TimeField()
    peticion_adicional = models.TextField(max_length=200, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO_RESERVACION, default='PC')
    fecha_reserva = models.DateTimeField(auto_now_add=True) #Fecha y hora de creación
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    habitacion = models.ManyToManyField(Habitacion, related_name='habitaciones')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=False)
    servicios = models.ManyToManyField(Servicio, related_name='servicios', help_text='Servicios incluidos')
