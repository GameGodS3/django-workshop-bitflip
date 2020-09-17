from django.shortcuts import render, redirect
from .forms import EventCreator
from .jsonwrite import CreateJson
import json, os
# Create your views here.

def renderjson():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('jsonfile.json', 'r') as f:
        jsonvar=json.load(f)['entries']
        print(jsonvar)
    eventlist = []
    for element in jsonvar:
        eventlist.append(element)
    eventlist.reverse()
    return eventlist

def index(request):
    return render(request, 'webpages/index.html')

def events(request):
    form = EventCreator(request.POST)
    eventlist = renderjson()
    if request.method == 'POST':
        if form.is_valid():
            evetitle = form.cleaned_data['eventtitle']
            evedesc = form.cleaned_data['eventdesc']
            print(evetitle, evedesc)
            CreateJson(evetitle, evedesc)
            return render(request, 'webpages/blank.html')
            #return render(request, 'webpages/events.html', {'form':form, 'eventlist':eventlist})
    else:
        return render(request, 'webpages/events.html', {'form':form, 'eventlist':eventlist})
        