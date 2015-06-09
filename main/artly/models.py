from django.db import models

class ArtInstallation(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(default="http://www.google.com/")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
