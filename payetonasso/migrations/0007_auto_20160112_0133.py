# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0006_nemopaytransaction_validation_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nemopaytransaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nemopaytransaction',
            name='validation_url',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
