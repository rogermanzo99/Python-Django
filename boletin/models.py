from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python2
		return self.email

