# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-05 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160805_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberlink',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='name',
        ),
        migrations.AddField(
            model_name='memberlink',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Social'), (1, 'Professional'), (2, 'Website / Blog'), (3, 'Other')], default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectlink',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Repository'), (1, 'Live App'), (2, 'Download Link'), (3, 'Other')], default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberskill',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Competent'), (4, 'Highly Experienced'), (5, 'Proficient')]),
        ),
    ]
