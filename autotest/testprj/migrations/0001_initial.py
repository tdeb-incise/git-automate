# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-03 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case_id', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(verbose_name='date time executed')),
                ('result', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
        ),
    ]
