from __future__ import unicode_literals
from django.db import models
from places.models import Location

class Adventure(models.Model):
	location = models.ForeignKey(Location)
	adventure_description = models.TextField(max_length=256)
	before_adventure = models.TextField(max_length=256)
	avoid_next_time = models.TextField(max_length=256)
	recommend_next_time = models.TextField(max_length=256)
