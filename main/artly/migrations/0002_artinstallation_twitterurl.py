# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artinstallation',
            name='twitterurl',
            field=models.URLField(default=b'http://www.google.com/'),
        ),
    ]
