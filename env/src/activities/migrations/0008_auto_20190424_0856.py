# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-24 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20190424_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['post_order', 'title']},
        ),
    ]
