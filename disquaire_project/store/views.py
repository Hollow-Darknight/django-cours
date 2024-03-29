from django.shortcuts import render, get_object_or_404

from .models import Album, Artist, Contact, Booking


def index (request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formattedAlbums = ["<li>{}</li>".format(album.title) for album in albums]
    context = {'albums': albums}
    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = {'albums': albums}
    return render(request, 'store/listing.html', context)


def detail(request, albumID):
    album = get_object_or_404(Album, pk=albumID)
    artists = album.artists.all()
    artists = " ".join([artist.name for artist in album.artists.all()])
    context = {
        'albumTitle': album.title,
        'artistsName': artists,
        'albumID': album.id,
        'thumbnail': album.picture
    }
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
           albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultat pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)