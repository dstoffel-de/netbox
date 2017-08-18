# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0001_initial'),
        ('dcim', '0041_napalm_integration'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='virtualization.Cluster'),
        ),
    ]
