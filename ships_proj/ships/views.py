from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'ships/ships.html')

def other(request):
    return HttpResponse('also works')

