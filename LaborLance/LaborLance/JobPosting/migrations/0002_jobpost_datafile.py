# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPosting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='datafile',
            field=models.FileField(default=None, upload_to=b''),
        ),
    ]