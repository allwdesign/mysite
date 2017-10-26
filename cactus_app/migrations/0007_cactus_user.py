# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 17:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cactus_app', '0006_auto_20170914_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='cactus',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]