# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20160531_1437'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CatGallery',
        ),
    ]
