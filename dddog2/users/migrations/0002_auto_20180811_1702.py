# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-11 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=200, null=True, verbose_name='密码'),
        ),
    ]
