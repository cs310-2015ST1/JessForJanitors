import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
django.setup()

from artly.models import ArtInstallation


def populate():
    
    add_art(name="Royal Sweet Diamond",
        url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=380&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;&lt;/a&gt;")

    add_art(name="Four Boats Stranded:  Red and Yellow, Black and White",
        url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=386&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Vancouver Art Gallery&lt;/a&gt;")

    add_art(name="Weave",
        url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=388&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;The Escala&lt;/a&gt;")

    # Print out what we have added to the user.
    for c in ArtInstallation.objects.all():
        print "- {0}".format(str(c))


def add_art(name, url):
    a = ArtInstallation.objects.get_or_create(name=name, url=url)[0]
    # a.save()
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting Artly population script..."
    populate()