# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 08:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegister', '0004_auto_20200426_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='locations',
            field=models.ManyToManyField(null=True, to='InitialMigrations.CityState'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='maxpay',
            field=models.FloatField(default=0.99, validators=[django.core.validators.MinValueValidator(0.99)]),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='minpay',
            field=models.FloatField(default=0.99, validators=[django.core.validators.MinValueValidator(0.99)]),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='skills',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
