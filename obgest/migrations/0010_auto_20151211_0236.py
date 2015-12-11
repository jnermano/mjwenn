# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0009_auto_20151102_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contact_email',
            field=models.EmailField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annonce',
            name='owner_email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
