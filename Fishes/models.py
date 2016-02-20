from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Store(models.Model):
	location = models.CharField(max_length = 255)
	timeOpen = models.TimeField()
	timeClose = models.TimeField()

	def __str__(self):
		returm self.location

class Fish(models.Model):
	name = models.CharField(max_length = 255)
	qiantity = models.IntegerField
	price = models.DecimalField(max_digits = 6, decimal_places = 2, default = 0)
	store = models.ForeignKey(Store, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

	def is_low_stock(self):
        return self.quantity < 10
