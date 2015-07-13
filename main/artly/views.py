from django.shortcuts import render
from django.http import HttpResponse
from artly.models import ArtInstallation
from artly.models import UserInformation

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by name
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    art_list = ArtInstallation.objects.order_by('name')
    saved_list = UserInformation.objects.order_by('name')
    context_dict = {'artinstallations': art_list, 'savedinstallations': saved_list}
#     context_dict2 = {'savedinstallations': saved_list}

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

def click_save(request):
    installation_name = None
    if request.method == 'GET':
        installation_name = request.GET['name']
    
    if installation_name:
        
        installation = ArtInstallation.objects.get(name=str(installation_name))
        
        if installation:
            if installation.selected:
                UserInformation.savedinstallations.add(installation)
            else:
                UserInformation.savedinstallations.remove(installation)
    return HttpResponse(installation.name)