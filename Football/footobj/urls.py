from django.urls import path, re_path

from footobj.views import index, FootballView, MinyFootballView, searchBar, \
    FootballDetailView, miny_footballs, MinyFootballDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'index'),
    path('football/', FootballView.as_view(),name='football'),
    path('football/<slug:slug>/',FootballDetailView.as_view(), name='footballs'),
    path('miny_football/', MinyFootballView.as_view(),name='miny_football'),
    path('miny_football/<slug:slug>/',MinyFootballDetailView.as_view(), name = 'miny_footballs'),
    path('search/', searchBar, name='search'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
