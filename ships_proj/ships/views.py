from django.shortcuts import render
from django.http import HttpResponse
from ships.models import Ship
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class Index(generic.ListView):
    model = Ship
    context_object_name = 'ships'
    template_name =  'ships/ships.html'


def other(request):
    return HttpResponse('also works')


class ShipDetailView(generic.DetailView):
    model = Ship
    context_object_name = 'ship'
    template_name = 'ships/ship_detail.html'
    

class ShipCreateView(generic.CreateView):
    model = Ship
    success_url = reverse_lazy('index')


class ShipUpdateView(generic.UpdateView):
    model = Ship
    success_url = reverse_lazy('index')


class ShipDeleteView(generic.DeleteView):
    model = Ship
    success_url = reverse_lazy('index')

