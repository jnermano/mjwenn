# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_annonce', models.IntegerField()),
                ('owner_first_name', models.CharField(max_length=50)),
                ('owner_last_name', models.CharField(max_length=50)),
                ('owner_email', models.CharField(max_length=50)),
                ('picture', models.CharField(max_length=255)),
                ('pub_date', models.DateField()),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_tel', models.CharField(max_length=20)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_place', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='obgest.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('date_signup', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='recovery',
            name='user',
            field=models.ForeignKey(to='obgest.User'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='category',
            field=models.ForeignKey(to='obgest.Category'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='recovery',
            field=models.ForeignKey(to='obgest.Recovery'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='type',
            field=models.ForeignKey(to='obgest.Type'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='user',
            field=models.ForeignKey(to='obgest.User'),
        ),
    ]
