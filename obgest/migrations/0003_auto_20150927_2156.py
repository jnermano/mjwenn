# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import obgest.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obgest', '0002_auto_20150925_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(default=b' ', max_length=100)),
                ('contact_tel', models.CharField(default=b' ', max_length=20)),
                ('contact_email', models.EmailField(default=b' ', max_length=254)),
                ('contact_place', models.CharField(default=b' ', max_length=255)),
                ('desc', models.CharField(default=b' ', max_length=255)),
                ('lat', models.DecimalField(null=True, max_digits=18, decimal_places=10, blank=True)),
                ('lon', models.DecimalField(null=True, max_digits=18, decimal_places=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_web', models.URLField()),
                ('avatar', models.FileField(null=True, upload_to=obgest.models.get_avatar_path, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='contact_place',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='contact_tel',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='desc',
        ),
        migrations.AddField(
            model_name='annonce',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='picture',
            field=models.FileField(upload_to=obgest.models.get_file_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to='obgest.Profile'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='address',
            field=models.ForeignKey(to='obgest.Address', null=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='user',
            field=models.ForeignKey(to='obgest.Profile', null=True),
        ),
    ]
