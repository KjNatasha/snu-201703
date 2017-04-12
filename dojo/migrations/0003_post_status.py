# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-12 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_auto_20170405_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdraw')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
