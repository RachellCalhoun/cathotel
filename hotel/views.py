from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import AboutUs, Gallery
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from blog.views import Notice

# Create your views here.
def our_hotel(request):
    ourhotels = AboutUs.objects.filter(category="Hotel")
    ourservice = AboutUs.objects.filter(category="Service")
    location = AboutUs.objects.filter(category="Location")
    questions = AboutUs.objects.filter(category="FAQ")
    return render(request, 'hotel/our_hotel.html', {'ourhotels': ourhotels, 'questions': questions, 'ourservice': ourservice, 'location': location})

def public(request):
	images = Gallery.objects.all()
	notices = Notice.objects.filter(privacy="Public").filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
	return render(request, 'hotel/home.html', {'images': images, 'notices': notices})

def gallery(request):
	images = Gallery.objects.all()
	return render(request, 'hotel/hotel_gallery.html', {'images': images})

def rooms(request):
 	hotel = Gallery.objects.filter(category="Hotel")
 	return render(request, 'hotel/rooms.html', {'hotel': hotel})

