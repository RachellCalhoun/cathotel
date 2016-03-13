# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='privacy',
            field=models.CharField(max_length=15, choices=[('Public', 'Public'), ('Private', 'Private')], default='Public'),
        ),
    ]
