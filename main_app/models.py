from django.db import models
from django.urls import reverse

from datetime import date

# Create your models here.
METHODS = (
    ('1', 'In the Car'),
    ('2', 'With Headphones'),
    ('3', 'In a Video')
)

class Instrument(models.Model):
    INSTRUMENT_TYPES = (
        ('S', 'Strings'),
        ('P', 'Percussion'),
        ('W', 'Woodwind'),
        ('B', 'Brass'),
        ('V', 'Vocals'),
    )
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    sound = models.CharField(max_length=1, choices=INSTRUMENT_TYPES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('instruments_detail', kwargs={'pk': self.id})


class Album(models.Model):
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    # M:M relationship
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})
    
    def listened_today(self):
        return self.listen_set.filter(date=date.today()).count() >= 0


class Listen(models.Model):
    date = models.DateTimeField('listen date')
    method = models.CharField(
        max_length=1, choices=METHODS, default=METHODS[0][0])
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"I listened to this album {self.get_method_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'Album Cover for: {self.album_id} @{self.url}'

