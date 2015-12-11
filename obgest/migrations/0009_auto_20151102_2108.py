# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0008_auto_20151102_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='owner_tel',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='ret_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.TextField(default=b' ', null=True, blank=True),
        ),
    ]
