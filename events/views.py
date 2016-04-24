from django.shortcuts import render
from events.models import Event
from django.utils import timezone


# Create your views here.
def LanderView(request):
    '''Show the three closest up coming events.'''
    events = Event.objects.order_by('-start_date')[:3]

    context = {'events': events}

    return render(request, 'frontpage.html', context)


def InspectionView(request):
    '''Inspect all events.'''
    events = Event.objects.all()

    context = {'events': events}

    return render(request, 'events_inspection.html', context)


def InspectEvent(request):
    '''Inspect/modify a single event.'''
    # Placeholder
    event1 = Event.objects.first()

    context = {'event1': event1}

    return render(request, 'event.html', context)