# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cactus_app', '0007_cactus_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RenameField(
            model_name='cactus',
            old_name='name',
            new_name='cactus_name',
        ),
    ]
