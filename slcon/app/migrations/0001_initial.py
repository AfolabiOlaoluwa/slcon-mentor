# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Mentee'), (1, 'Mentor')])),
                ('interests', models.ManyToManyField(to='app.Interest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemberLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(to='app.Member')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.PositiveSmallIntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='app.Skill'),
        ),
        migrations.AddField(
            model_name='member',
            name='skills',
            field=models.ManyToManyField(to='app.Skill'),
        ),
    ]
