from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import AboutUs, CatGallery, HotelGallery
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from blog.views import Notice

# Create your views here.
def our_hotel(request):
    ourhotels = AboutUs.objects.filter(category="Hotel")
    return render(request, 'hotel/our_hotel.html', {'ourhotels': ourhotels})


def our_service(request):
    ourservice = AboutUs.objects.filter(category="Service")
    return render(request, 'hotel/our_service.html', {'ourservice': ourservice})

def location(request):
    location = AboutUs.objects.filter(category="Location")
    return render(request, 'hotel/location.html', {'location': location})

def faq(request):
    questions = AboutUs.objects.filter(category="FAQ")
    return render(request, 'hotel/faq.html', {'questions': questions})

def cat_gallery(request):
	catimages = CatGallery.objects.all()
	return render(request, 'hotel/cat_gallery.html', {'catimages': catimages})

def public(request):
	catimages = CatGallery.objects.filter(category="Public")
	publichotelimages = HotelGallery.objects.filter(privacycategory="Public")
	notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:4]
	return render(request, 'hotel/home.html', {'catimages': catimages, 'publichotelimages': publichotelimages, 'notices': notices})

def hotel_gallery(request):
	hotelimages = HotelGallery.objects.all()
	return render(request, 'hotel/hotel_gallery.html', {'hotelimages': hotelimages})

def room_type1(request):
 	type1rooms = HotelGallery.objects.filter(category="Room1")
 	return render(request, 'hotel/room_type1.html', {'type1rooms': type1rooms})
def room_type2(request):
 	type2rooms = HotelGallery.objects.filter(category="Room2")
 	return render(request, 'hotel/room_type2.html', {'type2rooms': type2rooms})



