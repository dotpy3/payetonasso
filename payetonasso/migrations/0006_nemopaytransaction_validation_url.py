# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0005_auto_20151227_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='nemopaytransaction',
            name='validation_url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
