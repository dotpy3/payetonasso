# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('validation', models.DateTimeField(default=None, null=True)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NemopayTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 12, 25, 21, 23, 35, 627598))),
                ('nemopay_id', models.IntegerField(default=None, null=True)),
                ('inv_transaction', models.ForeignKey(to='payetonasso.IndividualTransaction')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('message', models.TextField(default=b'', blank=True)),
                ('nemopay_article_id', models.IntegerField(default=None, null=True)),
                ('price', models.IntegerField(default=0)),
                ('notify_creator', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 12, 25, 21, 23, 35, 625076))),
                ('creator', models.ForeignKey(related_name='user_generated_transactions_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
