# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_link',
            field=models.FileField(default='', upload_to='/uploads'),
        ),
    ]
