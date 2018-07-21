from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Event

def index(request):
    context = {
        'latest_events': Event.objects.all(),
    }
    return render(request, 'event/index.html', context)

def detail(request, event_id):
    return HttpResponse(f'Hello, {event_id}')
