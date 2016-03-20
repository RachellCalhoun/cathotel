from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.flatpages import views
from django_markdown import flatpages

admin.autodiscover()
flatpages.register()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('hotel.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^', include('blog.urls')),
    url(r'^(?P<url>.*/)$', views.flatpage),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
