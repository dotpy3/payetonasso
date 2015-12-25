# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nemopaytransaction',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
