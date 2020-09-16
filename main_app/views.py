from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Album, Instrument
from .forms import ListenForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    instruments_album_doesnt_have = Instrument.objects.exclude(
        id__in=album.instruments.all().values_list('id'))
    listen_form = ListenForm()
    return render(request, 'albums/detail.html', {'album': album, 'listen_form': listen_form, 'instruments': instruments_album_doesnt_have})


def add_listen(request, album_id):
    form = ListenForm(request.POST)
    if form.is_valid():
        new_listen = form.save(commit=False)
        new_listen.album_id = album_id
        new_listen.save()
    return redirect('detail', album_id=album_id)


def assoc_instrument(request, album_id, instrument_id):
    Album.objects.get(id=album_id).instruments.add(instrument_id)
    return redirect('detail', album_id=album_id)


def unassoc_instrument(request, album_id, instrument_id):
    Album.objects.get(id=album_id).instruments.remove(instrument_id)
    return redirect('detail', album_id=album_id)


class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    success_url = '/albums/'


class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'


class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'


class InstrumentList(ListView):
    model = Instrument


class InstrumentDetail(DetailView):
    model = Instrument


class InstrumentCreate(CreateView):
    model = Instrument
    fields = '__all__'


class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = '__all__'


class InstrumentDelete(DeleteView):
    model = Instrument
    success_url = '/instruments/'
