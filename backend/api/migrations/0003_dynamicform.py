# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160721_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dynamicform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField()),
                ('answers', models.TextField()),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamicforms', to='api.Grant')),
            ],
        ),
    ]
