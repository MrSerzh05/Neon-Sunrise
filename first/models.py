from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 20)
	email = models.TextField(max_length = 30)
	password = models.TextField(max_length = 20)