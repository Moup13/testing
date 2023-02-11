from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template import context
from django.views.generic import ListView, DetailView

from footobj.models import Football, MinyFootball


def index(request):
    return render(request, 'base.html')


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            football = Football.objects.filter(title__icontains=query)
            miny_football = MinyFootball.objects.filter(title__icontains=query)
            return render(request, 'base.html', {'football':football,
                                                      'miny_football':miny_football,
                                                 })
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

class FootballView(ListView):

    """Список футбола"""

    model = Football
class MinyFootballDetailView(DetailView):

    """Список минифутбола"""
    model = MinyFootball
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["minifoot_objects"] = MinyFootball.objects.all()

        return context





class FootballDetailView(DetailView):

    """Список футбола"""
    model = Football
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fot_objects"] = Football.objects.all()

        return context





class MinyFootballView(ListView):
    """Список минифутбола"""

    model = MinyFootball















def miny_footballs(request):
    current_link = '/miny_football/'
    one_new = get_object_or_404(Football, link=football)
    response = render(request, 'footobj/minyfootball_list.html', locals())
    response['Cache-Control'] = 'no-cache, must-revalidate'
    return response


