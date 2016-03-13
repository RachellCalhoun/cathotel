# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotelgallery_privacycategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='category',
            field=models.CharField(max_length=15, choices=[('Hotel', 'Hotel'), ('Service', 'Service'), ('Location', 'Location'), ('FAQ', 'FAQ')], default='Hotel'),
        ),
    ]
