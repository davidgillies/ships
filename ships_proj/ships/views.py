from django.shortcuts import render
from django.http import HttpResponse
from ships.models import Ship
from django.views import generic

# Create your views here.

#def index(request):
#    return render(request, 'ships/ships.html')

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

