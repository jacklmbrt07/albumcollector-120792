from django.db import models
from django.urls import reverse

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})


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
