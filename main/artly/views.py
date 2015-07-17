from django.shortcuts import render
from django.http import HttpResponse
from artly.models import ArtInstallation
from artly.models import ArtlyUser

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by name
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    art_list = ArtInstallation.objects.order_by('name')

    if request.user.is_authenticated():
        profile = request.user.artlyuser
        saved_list = profile.savedinstallations.all()
        context_dict = {'artinstallations': art_list, 'savedinstallations': saved_list}
    else:
        context_dict = {'artinstallations': art_list}

    # Render the response and send it back!
    return render(request, 'artly/index.html', context_dict)


def map(request):
    art_list = ArtInstallation.objects.order_by('-name')
    context_dict = {'artinstallations': art_list}

    return render(request, 'artly/map.html', context_dict)

"""
def click_toggle_favourites(request):
    return render(request)
"""