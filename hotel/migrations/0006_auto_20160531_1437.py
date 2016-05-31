# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20160313_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='hotel')),
                ('text', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=10, choices=[('Hotel', 'Hotel'), ('Cat', 'Cat')], default='Hotel')),
            ],
        ),
        migrations.DeleteModel(
            name='HotelGallery',
        ),
    ]
