# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payetonasso', '0002_auto_20151225_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualtransaction',
            name='state',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'V', b'Valid\xc3\xa9e'), (b'A', b'Annul\xc3\xa9e'), (b'W', b'En cours')]),
        ),
        migrations.AddField(
            model_name='nemopaytransaction',
            name='state',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'V', b'Valid\xc3\xa9e'), (b'A', b'Annul\xc3\xa9e'), (b'W', b'En cours')]),
        ),
    ]
