# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_usuariocategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='destinatario',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
