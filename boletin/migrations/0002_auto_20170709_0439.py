# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-09 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
