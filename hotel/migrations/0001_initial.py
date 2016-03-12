# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='', null=True, blank=True)),
                ('category', models.CharField(max_length=15, choices=[('Service', 'Service'), ('Hotel', 'Hotel'), ('Location', 'Location')], default='Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='CatGallery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='cats')),
                ('text', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelGallery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='hotel')),
                ('text', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
