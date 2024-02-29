from django.contrib import admin
from .models import Album, Artist, Released, Genre, Company
# Δηλώνουμε τα μοντέλα που θα βλέπει ο διαχειριστής στην σελίδα του.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Released)
admin.site.register(Genre)
admin.site.register(Company)
