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

class HotelGallery(models.Model):
	title = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="hotel")
	text = models.TextField(blank=True, null=True)
	ROOM1 = "Room1"
	ROOM2 = "Room2"
	OTHER = "Other"
	POSTCATEGORY = (
		(ROOM1, "Room1"),
		(ROOM2, "Room2"),
		(OTHER, "Other"),
		)
	category = models.CharField(max_length=10, choices=POSTCATEGORY, default=OTHER)
	PRIVATE = "Private"
	PUBLIC = "Public"
	PRIVACYCATEGORY = (
		(PRIVATE, "Private"),
		(PUBLIC, "Public"),
		)
	privacy = models.CharField(max_length=10, choices=PRIVACYCATEGORY, default=PRIVATE)

	def __str__(self):
		return self.title

class CatGallery(models.Model):
	title = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="cats")
	text = models.TextField(blank=True, null=True)
	PRIVATE = "Private"
	PUBLIC = "Public"
	POSTCATEGORY = (
		(PRIVATE, "Private"),
		(PUBLIC, "Public"),
		)
	category = models.CharField(max_length=10, choices=POSTCATEGORY, default=PRIVATE)

	def __str__(self):
		return self.title
