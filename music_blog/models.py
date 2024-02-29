from django.db import models


# Το μοντέλο του Άλμπουμ που είναι και το βασικό μας
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_year = models.ForeignKey('Released', null=True, on_delete=models.CASCADE)
    album_img = models.ImageField(null=True)
    album_songs = models.TextField(null=True)
    album_genre = models.ForeignKey('Genre', null=True, on_delete=models.CASCADE)
    album_artist = models.ForeignKey('Artist', null=True, on_delete=models.CASCADE)
    album_comp = models.ForeignKey('Company', null=True, on_delete=models.CASCADE)

    # Εμφανίζει το όνομα του αλμπουμ όταν καλούμε το συγκεκριμένο μοντέλο.
    def __str__(self):
        return self.album_name

    # Ταξινόμηση του μοντέλου με βάση το όνομα.
    class Meta:
        ordering = ('album_name',)


# Το μοντέλο του καλλιτέχνη
class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_img = models.ImageField(null=True)
    artist_bio = models.TextField(null=True)
    artist_url = models.CharField(max_length=50, null=True, default="#")
    artist_discography = models.TextField(null=True)

    # Εμφανίζει το όνομα του καλλιτέχνη όταν καλούμε το συγκεκριμένο μοντέλο.
    def __str__(self):
        return self.artist_name

    # Ταξινόμηση του μοντέλου με βάση το όνομα.
    class Meta:
        ordering = ('artist_name',)


# Το μοντέλο της εταιρίας
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_info = models.CharField(max_length=50)
    company_bio = models.TextField(null=True)

    # Εμφανίζει το όνομα της εταιρίας όταν καλούμε το συγκεκριμένο μοντέλο.
    def __str__(self):
        return self.company_name

    # Ταξινόμηση του μοντέλου με βάση το όνομα.
    class Meta:
        ordering = ('company_name',)


# Το μοντέλο του είδους
class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    # Εμφανίζει το όνομα του είδους όταν καλούμε το συγκεκριμένο μοντέλο.
    def __str__(self):
        return self.genre_name

    # Ταξινόμηση του μοντέλου με βάση το όνομα.
    class Meta:
        ordering = ('genre_name',)


# Το μοντέλο της έκδοσης
class Released(models.Model):
    Released_name = models.IntegerField(default=1990)

    # Εμφανίζει την χρονολογία όταν καλούμε το συγκεκριμένο μοντέλο.
    def __str__(self):
        return str(self.Released_name)

    # Ταξινόμηση του μοντέλου με βάση την χρονολογία.
    class Meta:
        ordering = ('Released_name',)
