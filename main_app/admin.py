from django.contrib import admin

from .models import Album, Listen, Instrument

# Register your models here.
admin.site.register(Album)
admin.site.register(Instrument)
admin.site.register(Listen)
