# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-26 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegister', '0003_auto_20200425_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='locations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='InitialMigrations.CityState'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
