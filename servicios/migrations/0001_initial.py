# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(max_length=1, choices=[('a', 'Archivo'), ('f', 'Fondo'), ('s', 'Secci\xf3n'), ('e', 'Serie')])),
                ('padre', models.ForeignKey(related_name='Jerarquia', blank=True, to='servicios.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expediente', models.CharField(max_length=200)),
                ('fechaEntrega', models.DateField()),
                ('fechaDevolucion', models.DateField(null=True, blank=True)),
                ('tipo', models.CharField(max_length=1, choices=[('p', 'Pr\xe9stamo'), ('c', 'Copia'), ('o', 'Consulta')])),
                ('fondo', models.ForeignKey(related_name='fondo', to='servicios.Categoria')),
                ('seccion', models.ForeignKey(related_name='seccion', blank=True, to='servicios.Categoria', null=True)),
                ('serie', models.ForeignKey(related_name='serie', blank=True, to='servicios.Categoria', null=True)),
                ('usuarioEntrega', models.ForeignKey(related_name='usr_prestamo', to=settings.AUTH_USER_MODEL)),
                ('usuarioRecibe', models.ForeignKey(related_name='usr_recibe', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
