# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtInstallation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locationid', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(default=b'http://www.google.com/')),
                ('lat', models.FloatField(default=49.2508548)),
                ('lon', models.FloatField(default=-123.1174762)),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
