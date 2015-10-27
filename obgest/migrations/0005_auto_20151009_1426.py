# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import obgest.models


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0004_auto_20150927_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(default=b'avatars/user1.png', null=True, upload_to=obgest.models.get_avatar_path, blank=True),
        ),
    ]
