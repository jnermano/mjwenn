# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obgest', '0007_profile_hach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='secret_reponse',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='secret_question',
            field=models.OneToOneField(null=True, to='obgest.Question'),
        ),
    ]
