# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Release')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.TextField()),
                ('benefit', models.TextField()),
                ('due_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
                ('points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Point')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Role')),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sprint')),
                ('tags', models.ManyToManyField(to='main.Tag')),
            ],
        ),
    ]