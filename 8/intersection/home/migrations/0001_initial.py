# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=10)),
                ('Phone', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='User_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('modified', models.DateField(auto_now=True)),
                ('email_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
    ]
