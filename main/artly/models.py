from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class ArtInstallation(models.Model):
    locationid = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    url = models.URLField(default="http://www.google.com/")
    lat = models.FloatField(default=49.2508548)
    lon = models.FloatField(default=-123.1174762)
    twitterurl = models.URLField(default="http://www.twitter.com/")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class ArtlyUser(models.Model):
    user = models.OneToOneField(User)
    savedinstallations = models.ManyToManyField(ArtInstallation, null=True, blank=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user.username

def create_artly_user(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = ArtlyUser(user=user)
        up.save()

post_save.connect(create_artly_user, sender=User)