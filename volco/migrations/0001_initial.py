# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='volco',
            fields=[
                ('id_volco', models.AutoField(primary_key=True, serialize=False)),
                ('Placa', models.CharField(max_length=50)),
                ('Chofer', models.CharField(max_length=100)),
            ],
        ),
    ]