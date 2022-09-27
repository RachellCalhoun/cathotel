from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^ourhotel/$', views.our_hotel, name='our_hotel'),
    re_path(r'^gallery/$', views.gallery, name='gallery'),
    re_path(r'^rooms/$', views.rooms, name='rooms'),
    re_path(r'^$', views.public, name='home'),
]

app_name = 'hotel'