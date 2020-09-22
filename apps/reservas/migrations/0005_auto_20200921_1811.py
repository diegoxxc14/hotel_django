# Generated by Django 2.2 on 2020-09-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_reservacion_pagada'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicioIncluido',
            new_name='Servicio',
        ),
        migrations.RemoveField(
            model_name='reservacion',
            name='servicio_incluido',
        ),
        migrations.AddField(
            model_name='reservacion',
            name='servicios',
            field=models.ManyToManyField(help_text='Servicios incluidos', related_name='servicios', to='reservas.Servicio'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.CharField(max_length=4, verbose_name='Número:'),
        ),
    ]
