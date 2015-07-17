__author__ = 'Stephen'
from django.views.decorators.csrf import csrf_exempt
from artly.models import ArtInstallation

@csrf_exempt
def toggle_favourites(request):

    profile = request.user.artlyuser

    if request.method == 'POST':
        locationid = request.POST['locationid']

    if locationid:
        if profile.savedinstallations.filter(locationid=locationid).exists():
            profile.savedinstallations.through.objects.filter(artinstallation=profile.savedinstallations.filter(locationid=locationid)[:1].get(),artlyuser=profile).delete();
        else:
            art = ArtInstallation.objects.filter(locationid=locationid)[:1].get()
            art.save()
            profile.savedinstallations.add(art)
            profile.save()