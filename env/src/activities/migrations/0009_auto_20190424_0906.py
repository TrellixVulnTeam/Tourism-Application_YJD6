# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-24 08:06
from __future__ import unicode_literals

import activities.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20190424_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='post_order',
            field=activities.fields.PositionField(default=-1),
        ),
    ]
