# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_servicio_destinatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='fechaEntrega',
            field=models.DateField(auto_now_add=True),
        ),
    ]
