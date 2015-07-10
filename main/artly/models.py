from django.db import models

class ArtInstallation(models.Model):
    locationid = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    url = models.URLField(default="http://www.google.com/")
    lat =  models.FloatField(default=49.2508548)
    lon = models.FloatField(default=-123.1174762)
    selected = models.BooleanField(default=False)
    favourited = models.BooleanField(default=False)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class UserInformation(models.Model):
    userid = models.CharField(max_length=128, unique=True)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    savedinstallations = models.CommaSeparatedIntegerField(max_length=512)
    