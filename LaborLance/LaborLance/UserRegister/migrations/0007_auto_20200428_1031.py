# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 10:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserRegister', '0006_auto_20200428_1017'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='business',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='jobseeker',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='business',
            name='id',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='id',
        ),
        migrations.AddField(
            model_name='business',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=38, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='location',
            field=models.ManyToManyField(to='InitialMigrations.CityState'),
        ),
    ]
