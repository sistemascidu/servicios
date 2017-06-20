# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.ForeignKey(related_name='categoria_usuario', to='servicios.Categoria')),
                ('usuario', models.ForeignKey(related_name='usuario_categoria', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
