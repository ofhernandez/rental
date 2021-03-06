# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('image', models.FileField(null=True, upload_to='complaints')),
            ],
        ),
    ]
