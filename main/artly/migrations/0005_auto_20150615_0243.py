# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artly', '0004_auto_20150610_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artinstallation',
            name='lat',
            field=models.FloatField(default=49.2508548),
        ),
        migrations.AlterField(
            model_name='artinstallation',
            name='lon',
            field=models.FloatField(default=-123.1174762),
        ),
    ]
