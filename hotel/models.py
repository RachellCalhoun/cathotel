from django.db import models
from django.utils import timezone

# Create your models here.
class AboutUs(models.Model):
	text = models.TextField(blank=True, null=True)
	title = models.CharField(max_length=200)
	photo = models.ImageField(blank=True, null=True)
	HOTEL = "Hotel"
	SERVICE = "Service"
	LOCATION = "Location"
	FAQ = "FAQ"
	POSTCATEGORY = (
		(HOTEL, 'Hotel'),
		(SERVICE, 'Service'),
		(LOCATION, 'Location'),
		(FAQ, 'FAQ'),
		)
	category = models.CharField(max_length=15, choices=POSTCATEGORY, default=HOTEL)


	def __str__(self):
		return self.title

class Gallery(models.Model):
	title = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="hotel")
	text = models.TextField(blank=True, null=True)
	HOTEL = "Hotel"
	CAT = "Cat"
	POSTCATEGORY = (
		(HOTEL, "Hotel"),
		(CAT, "Cat"),
		)
	category = models.CharField(max_length=10, choices=POSTCATEGORY, default=HOTEL)

	def __str__(self):
		return self.title
