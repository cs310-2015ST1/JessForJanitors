from django.contrib import admin
from artly.models import ArtInstallation
from artly.models import ArtlyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(ArtInstallation)
admin.site.register(ArtlyUser)