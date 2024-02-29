from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Company
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Εμφανίζει την σελίδα με τα Άλμπουν ανα 12άδες και κάνει την αναζήτηση.
def album_list(request):

    # Έλεγχος αν υπάρχει κείμενο προς αναζήτηση.
    txt = request.GET.get('txt', '')
    try:
        txt = str(txt)
    except:
        txt = False

        # Αν το κείμενο της αναζήτησης είναι κενό τρέχει ο παρακάτω κώδικας για να μας εμφανίσει όλα τα Άλμπουμ
        # ανα 12άδες.
    if txt == '':
        page_albums = Album.objects.order_by('album_name')
        paginator = Paginator(page_albums, 12)
        page = request.GET.get('page')
        try:
            albums = paginator.page(page)
        except PageNotAnInteger:
            albums = paginator.page(1)
        except EmptyPage:
            albums = paginator.page(paginator.num_pages)
    else:
        # Αν το κείμενο της αναζήτησης δεν είναι κενό τρέχει ο παρακάτω κώδικας για να μας εμφανίζει όλα τα Άλμπουν μετά
        # απο το φιλτράρισμα ανα 12άδες.
        # Εδώ γίνεται η αναζήτηση.
        page_albums = Album.objects.filter(Q(album_name__contains=txt) | Q(album_artist__artist_name__contains=txt)
                                           | Q(album_songs__contains=txt) | Q(album_genre__genre_name__contains=txt))

        paginator = Paginator(page_albums, 12)
        page = request.GET.get('page')
        try:
            albums = paginator.page(page)
        except PageNotAnInteger:
            albums = paginator.page(1)
        except EmptyPage:
            albums = paginator.page(paginator.num_pages)

    # Εδώ γίνεται η εμφάνιση των Άλμπουμ.
    return render(request, 'music_blog/album_list.html', {'albums': albums})


# Εμφανίζει την σελίδα με τα στοιχεία του Άλμπουμ.
def music_detail(request, pk):
    album_pk = get_object_or_404(Album, pk=pk)
    return render(request, 'music_blog/music_detail.html', {'album_pk': album_pk})


# Εμφανίζει την σελίδα με τα στοιχεία του Καλλιτέχνη.
def artist_detail(request, pk):
    art_pk = get_object_or_404(Artist, pk=pk)
    return render(request, 'music_blog/artist_detail.html', {'art_pk': art_pk})


# Εμφανίζει την σελίδα με τα στοιχεία των Εταιριών.
def company_detail(request, pk):
    comp_pk = get_object_or_404(Company, pk=pk)
    return render(request, 'music_blog/company_detail.html', {'comp_pk': comp_pk})

