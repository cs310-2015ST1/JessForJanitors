from django.shortcuts import render
from artly.models import ArtInstallation
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_auth.backends.exceptions import AuthFailed
from social_auth.views import complete


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by name
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    art_list = ArtInstallation.objects.order_by('name')
    context_dict = {'artinstallations': art_list}

    # Render the response and send it back!
    return render(request, 'artly/index.html', context_dict)


def map(request):
    art_list = ArtInstallation.objects.order_by('-name')
    context_dict = {'artinstallations': art_list}

    return render(request, 'artly/map.html', context_dict)

def click_installation(request):
    installation_name = None
    if request.method == 'GET':
        installation_name = request.GET['name']

    if installation_name:

        # get the installation
        installation = ArtInstallation.objects.get(name=str(installation_name))

        # flip the installation's selected boolean
        if installation:
            if installation.selected:
                installation.selected = False
            else:
                installation.selected = True

    return HttpResponse(installation.name)


class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backend')
        try:
            return complete(request, backend, *args, **kwargs)
        except AuthFailed:
            messages.error(request, "Your Google Apps domain isn't authorized for this app")
            return HttpResponseRedirect(reverse('login'))


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)