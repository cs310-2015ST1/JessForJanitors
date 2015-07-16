# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artly', '0005_auto_20150715_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artlyuser',
            name='savedinstallations',
            field=models.ManyToManyField(to=b'artly.ArtInstallation', null=True, blank=True),
        ),
    ]
