# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegister', '0005_auto_20200428_0834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobseeker',
            old_name='locations',
            new_name='location',
        ),
    ]