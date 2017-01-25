# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-06 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160806_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorship',
            name='skills',
        ),
        migrations.AddField(
            model_name='mentorship',
            name='skills',
            field=models.ManyToManyField(to='app.Skill'),
        ),
    ]