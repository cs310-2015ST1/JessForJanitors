import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
django.setup()

from artly.models import ArtInstallation

def populate():

    add_art(name="Royal Sweet Diamond",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=380&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;&lt;/a&gt;",
            lat=49.281273,
            lon=-123.115823)

    add_art(name="Four Boats Stranded:  Red and Yellow, Black and White",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=386&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Vancouver Art Gallery&lt;/a&gt;",
            lat=49.282932,
            lon=-123.120415)

    add_art(name="Weave",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=388&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;The Escala&lt;/a&gt;",
            lat=49.29068,
            lon=-123.124115)

    add_art(name="Curtained Skies",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=390&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Bayview&lt;/a&gt;",
            lat=49.290167,
            lon=-123.129083)

    add_art(name="Watch Your Step",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=400&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;David Lam Park&lt;/a&gt;",
            lat=49.272579,
            lon=-123.122657)

    add_art(name="Leaf Stream",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=394&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Bayshore tower&lt;/a&gt;",
            lat=49.29068,
            lon=-123.131793)

    add_art(name="New Sights in the Heights",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=426&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Champlain Heights Elementary School&lt;/a&gt",
            lat=49.220697,
            lon=-123.027485)

    add_art(name="Chinatown Millennium Gate",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=397&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Keefer&lt;/a&gt",
            lat=49.280719,
            lon=-123.105193)

    add_art(name="Roller",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=408&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;National  Works Yard&lt;/a&gt;",
            lat=49.273621,
            lon=-123.092675)

    add_art(name="Country Living in the City",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=417&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Champlain Heights Community Centre&lt;/a&gt;",
            lat=49.214854,
            lon=-123.032018)

    add_art(name="Footprints",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=423&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Downtown Eastside&lt;/a&gt;",
            lat=49.281071,
            lon=-123.10006)

    add_art(name="Marking High Tide and Waiting for Low Tide Pavillions",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=425&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;David Lam Park&lt;/a&gt;",
            lat=49.271847,
            lon=-123.12491)

    add_art(name="Semaphores",
            url="https://app.vancouver.ca/PublicArt_Net/ArtworkDetails.aspx?ArtworkID=428&amp;Neighbourhood=&amp;Ownership=&amp;Program='&gt;Harbour Green&lt;/a&gt;",
            lat=49.28967,
            lon=-123.123477)

    # Print out what we have added to the user.
    for c in ArtInstallation.objects.all():
        print "- {0}".format(str(c))

def add_art(name, lat, lon, url):
    a = ArtInstallation.objects.get_or_create(name=name, url=url, lat=lat, lon=lon)[0]
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting Artly population script..."
    populate()