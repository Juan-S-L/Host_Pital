# Generated by Django 4.2 on 2023-05-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medios_internos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcliente',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualización'),
        ),
    ]
