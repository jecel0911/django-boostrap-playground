from __future__ import unicode_literals
from django.db import models
from adventures.models import Adventure

class Picture(models.Model):
	adventure = models.ForeignKey(Adventure)
	img = models.ImageField(upload_to='pictures')
	description = models.CharField(max_length=50)
	funny_facts = models.TextField(max_length=256)