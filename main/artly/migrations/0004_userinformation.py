# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artly', '0003_auto_20150712_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(unique=True, max_length=128)),
                ('savedinstallations', models.ManyToManyField(to='artly.ArtInstallation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
