# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recovery',
            name='user',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='recovery',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='user',
        ),
        migrations.AddField(
            model_name='annonce',
            name='contact_email',
            field=models.EmailField(default=b' ', max_length=254),
        ),
        migrations.AddField(
            model_name='annonce',
            name='contact_name',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AddField(
            model_name='annonce',
            name='contact_place',
            field=models.CharField(default=b' ', max_length=255),
        ),
        migrations.AddField(
            model_name='annonce',
            name='contact_tel',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='desc',
            field=models.CharField(default=b' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='owner_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='picture',
            field=models.FileField(upload_to=b'%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Recovery',
        ),
    ]
