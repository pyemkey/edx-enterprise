# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0049_auto_20180531_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomerreportingconfiguration',
            name='data_type',
            field=models.CharField(choices=[('progress', 'progress'), ('progress_v2', 'progress_v2'), ('catalog', 'catalog')], default='progress', help_text='The type of data this report should contain.', max_length=20, verbose_name='Data Type'),
        ),
    ]
