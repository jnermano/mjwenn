# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0003_auto_20150927_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 2, 2, 58, 190000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
