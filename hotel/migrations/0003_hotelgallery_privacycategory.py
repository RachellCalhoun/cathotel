# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20160309_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelgallery',
            name='privacycategory',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], max_length=10, default='Private'),
        ),
    ]
