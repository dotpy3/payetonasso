# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0003_auto_20151225_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualtransaction',
            name='transaction',
            field=models.ForeignKey(to='payetonasso.Transaction', null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='fundation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='individualtransaction',
            name='user_email',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='individualtransaction',
            name='user_name',
            field=models.CharField(max_length=256),
        ),
    ]
