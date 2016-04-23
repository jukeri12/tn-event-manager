from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Generic info
    name = models.CharField(u'First and last name', max_length=255)
    phone = models.CharField(u'Phone number', null=True, blank=True, max_length=35)
    email = models.EmailField(u'E-mail address', null=True, blank=True)
    about = models.TextField(u'Description of me', null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='upload/')

    # TODO: More in the future if need be

    # DB things
    owner = models.OneToOneField(User)

    def __unicode__(self):
        return '%s (%s)', (self.name, self.phone)
