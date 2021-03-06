from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path('albums/', views.albums_index, name='index'),
    path('albums/<int:album_id>/', views.albums_detail, name='detail'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update/',
         views.AlbumUpdate.as_view(), name='albums_update'),
    path('albums/<int:pk>/delete/',
         views.AlbumDelete.as_view(), name='albums_delete'),
    path('instruments/', views.InstrumentList.as_view(), name='instruments_index'),
    path('instruments/<int:pk>/',
         views.InstrumentDetail.as_view(), name='instruments_detail'),
    path('instruments/create/', views.InstrumentCreate.as_view(),
         name='instruments_create'),
    path('instruments/<int:pk>/update/',
         views.InstrumentUpdate.as_view(), name='instruments_update'),
    path('instruments/<int:pk>/delete/',
         views.InstrumentDelete.as_view(), name='instruments_delete'),
    path('albums/<int:album_id>/add_listen/',
         views.add_listen, name='add_listen'),
    path('albums/<int:album_id>/assoc_instrument/<int:instrument_id>/',
         views.assoc_instrument, name='assoc_instrument'),
    path('albums/<int:album_id>/unassoc_instrument/<int:instrument_id>/',
         views.unassoc_instrument, name='unassoc_instrument'),
    path('albums/<int:album_id>/add_photo/',
         views.add_photo, name='add_photo'),
     path('accounts/signup/', views.signup, name='signup')
]
