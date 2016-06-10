# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='gallery')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spanish_name', models.CharField(max_length=255, unique=True)),
                ('english_name', models.CharField(max_length=255, unique=True)),
                ('french_name', models.CharField(max_length=255, unique=True)),
                ('german_name', models.CharField(max_length=255, unique=True)),
                ('portuguese_name', models.CharField(max_length=255, unique=True)),
                ('spanish_description', models.TextField(null=True)),
                ('english_description', models.TextField(null=True)),
                ('french_description', models.TextField(null=True)),
                ('german_description', models.TextField(null=True)),
                ('portuguese_description', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Service'),
        ),
    ]
