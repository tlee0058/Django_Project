# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20180401_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posters', to='login.Userdb'),
        ),
    ]
