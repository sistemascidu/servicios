# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_auto_20170324_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='oficio',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
    ]
