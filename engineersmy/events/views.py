from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from core.models import Event
from .forms import EventForm

def index(request):
    today = datetime.now().date()
    latest_events = (Event.objects
        .filter(date__gt=today)
        .filter(is_approved=True)
        .order_by('date'))[:5]
    # latest_events = []
    return render(request, 'index.html', {
        'latest_events': latest_events
    })

def detail(request, event_id):
    return HttpResponse(f'Hello, {event_id}')

def suggest(request):
    form = EventForm()
    return render(request, 'suggest.html', {
        'form': form,
    })