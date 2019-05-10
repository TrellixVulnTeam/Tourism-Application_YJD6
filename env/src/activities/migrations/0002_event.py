# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-23 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190422_1008'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('latest_update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.Activity')),
                ('video_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Post')),
            ],
        ),
    ]
