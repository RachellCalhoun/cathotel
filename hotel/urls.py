from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^ourhotel/$', views.our_hotel, name='our_hotel'),
    url(r'^ourservice/$', views.our_service, name='our_service'),
    url(r'^location/$', views.location, name='location'),
    url(r'^hotelgallery/$', views.hotel_gallery, name='hotelgallery'),
    url(r'^catgallery/$', views.cat_gallery, name='catgallery'),
    url(r'^roomtype1/$', views.room_type1, name='roomtype1'),
    url(r'^roomtype2/$', views.room_type2, name='roomtype2'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^$', views.public, name='home'),
]
