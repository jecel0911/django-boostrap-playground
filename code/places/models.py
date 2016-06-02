from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=50)

class Location(models.Model):
	country = models.ForeignKey(Country)
	funny_facts = models.TextField(max_length=256)


