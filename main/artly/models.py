from django.db import models
from django.contrib.auth.models import User

class ArtInstallation(models.Model):
    locationid = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    url = models.URLField(default="http://www.google.com/")
    lat = models.FloatField(default=49.2508548)
    lon = models.FloatField(default=-123.1174762)
    selected = models.BooleanField(default =False)
    twitterurl = models.URLField(default="http://www.twitter.com/")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class UserInformation(models.Model):
    user = models.OneToOneField(User)
    savedinstallations = models.ManyToManyField(ArtInstallation)
