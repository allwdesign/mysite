# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('flowers', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
    ]
