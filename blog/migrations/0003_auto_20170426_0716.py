# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
