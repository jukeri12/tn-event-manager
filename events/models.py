from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from users.models import UserProfile


class Address(models.Model):
    '''A location.'''
    address_line1 = models.CharField(u'Address Line 1', max_length=255)
    address_line2 = models.CharField(u'Address Line 2', max_length=255)
    city = models.CharField(u'City', max_length=255)
    postal_code = models.CharField(max_length=5)


class Event(models.Model):
    '''Generic event model.'''
    # Generic information on Event.
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(UserProfile, related_name='events')
    type_of_event = models.CharField(u'Type of event', max_length=255)
    description = models.TextField(u'Description of event')
    location = models.ForeignKey(Address, related_name='events')

    # Date information
    start_date = models.DateTimeField(u'Start date of event', default=timezone.now())
    end_date = models.DateTimeField(u'(Optional) end date for event', blank=True, null=True)

    # More specific information
    places_close_by = models.TextField(u'Interesting/useful places (e.g shops) nearby')
    things_to_take_note_of = models.TextField(u'Things to take note of (e.g existing debts for you cheapskates)')
    extra_information = models.TextField(u'Additional information')

    # Attendees
    attendees = models.ManyToManyField(UserProfile, related_name='attending')
    people_needing_a_ride = models.ManyToManyField(UserProfile, related_name='needs_ride_for')
    people_offering_rides = models.ManyToManyField(UserProfile, related_name='offering_rides_for')

    # Price on event
    sum_price = models.DecimalField(u'Price of event in total', max_digits=10, decimal_places=2, default=0.00)
    entry_price = models.DecimalField(u'Price for entering', max_digits=10, decimal_places=2, default=0.00)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.type_of_event)