# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170726_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]