from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class HTW(models.Model):
	"""

	"""
	target_temperature = models.IntegerField()
	ambient_temperature = models.IntegerField()
	ambient_humidity = models.FloatField()
	wind_speed = models.FloatField()
	record_datetime = models.DateTimeField()

	def get_absolute_url():
		return reverse('htw_list')
