from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^ourhotel/$', views.our_hotel, name='our_hotel'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^rooms/$', views.rooms, name='rooms'),
    url(r'^$', views.public, name='home'),
]
