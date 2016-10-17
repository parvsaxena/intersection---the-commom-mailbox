# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20161016_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='', max_length=256)),
                ('msg_id', models.CharField(max_length=256)),
                ('html_body', models.TextField(default='')),
                ('plain_body', models.TextField(default='')),
                ('date', models.CharField(max_length=30)),
                ('snippet', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('user_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User_id')),
            ],
        ),
    ]
