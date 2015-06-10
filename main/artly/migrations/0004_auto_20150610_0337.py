# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artly', '0003_auto_20150609_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='artinstallation',
            name='lat',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artinstallation',
            name='lon',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
