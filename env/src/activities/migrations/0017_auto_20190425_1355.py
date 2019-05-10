# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-25 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('activities', '0016_activity_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='category_example',
        ),
        migrations.AddField(
            model_name='activity',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_genre', to='categories.Genre'),
        ),
    ]