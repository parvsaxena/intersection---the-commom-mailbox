# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161013_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_id',
            name='email_id',
            field=models.CharField(default='hello', max_length=20),
            preserve_default=False,
        ),
    ]
