# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20160313_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelgallery',
            old_name='privacycategory',
            new_name='privacy',
        ),
    ]
