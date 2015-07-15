# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artly', '0004_userinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtlyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('savedinstallations', models.ManyToManyField(to='artly.ArtInstallation')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='savedinstallations',
        ),
        migrations.DeleteModel(
            name='UserInformation',
        ),
        migrations.RemoveField(
            model_name='artinstallation',
            name='selected',
        ),
    ]
