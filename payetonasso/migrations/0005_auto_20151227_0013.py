# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0004_auto_20151226_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='fundation_name',
            field=models.CharField(default=b'PayUTC', max_length=256),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
