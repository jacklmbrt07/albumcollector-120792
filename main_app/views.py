from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

from .models import Album, Instrument, Photo
from .forms import ListenForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'albumcollector-120792'


# Create your views here.
class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = '__all__'


class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = '/albums/'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def albums_index(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, 'albums/index.html', {'albums': albums})


@login_required
def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    instruments_album_doesnt_have = Instrument.objects.exclude(
        id__in=album.instruments.all().values_list('id'))
    listen_form = ListenForm()
    return render(request, 'albums/detail.html', {'album': album, 'listen_form': listen_form, 'instruments': instruments_album_doesnt_have})


@login_required
def add_listen(request, album_id):
    form = ListenForm(request.POST)
    if form.is_valid():
        new_listen = form.save(commit=False)
        new_listen.album_id = album_id
        new_listen.save()
    return redirect('detail', album_id=album_id)


@login_required
def add_photo(request, album_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, album_id=album_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')

    return redirect('detail', album_id=album_id)


@login_required
def assoc_instrument(request, album_id, instrument_id):
    Album.objects.get(id=album_id).instruments.add(instrument_id)
    return redirect('detail', album_id=album_id)


@login_required
def unassoc_instrument(request, album_id, instrument_id):
    Album.objects.get(id=album_id).instruments.remove(instrument_id)
    return redirect('detail', album_id=album_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class InstrumentList(LoginRequiredMixin, ListView):
    model = Instrument


class InstrumentDetail(LoginRequiredMixin, DetailView):
    model = Instrument


class InstrumentCreate(LoginRequiredMixin, CreateView):
    model = Instrument
    fields = '__all__'


class InstrumentUpdate(LoginRequiredMixin, UpdateView):
    model = Instrument
    fields = '__all__'


class InstrumentDelete(LoginRequiredMixin, DeleteView):
    model = Instrument
    success_url = '/instruments/'
