from django.conf.urls import url
from . import views
# Εδώ γίνεται η επιλογή του URL που θα ανοίξει ανάλογα με τις ενέργειε; του χρήστη.
urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    url(r'^Album/(?P<pk>[0-9]+)/$', views.music_detail, name='music_detail'),
    url(r'^ArtDet/(?P<pk>[0-9]+)/$', views.artist_detail, name='artist_detail'),
    url(r'^CompDet/(?P<pk>[0-9]+)/$', views.company_detail, name='company_detail'),
]