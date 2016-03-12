# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catgallery',
            name='category',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=10),
        ),
        migrations.AddField(
            model_name='hotelgallery',
            name='category',
            field=models.CharField(choices=[('Room1', 'Room1'), ('Room2', 'Room2'), ('Other', 'Other')], default='Other', max_length=10),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='category',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Service', 'Service'), ('Location', 'Location')], default='Hotel', max_length=15),
        ),
    ]
