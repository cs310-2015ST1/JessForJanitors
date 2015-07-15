from django.contrib import admin
from artly.models import ArtInstallation
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(ArtInstallation)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = ArtlyUser
    can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)