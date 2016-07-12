# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 12:55
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_link', models.FileField(default='', upload_to=api.models.upload_to)),
            ],
        ),
    ]