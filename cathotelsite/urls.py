from django.urls import include, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.flatpages import views


admin.autodiscover()


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^', include('hotel.urls', namespace='hotel')),
    re_path(r'^', include('accounts.urls', namespace='accounts')),
    re_path(r'^', include('blog.urls', namespace='blog')),
    re_path(r'^(?P<url>.*/)$', views.flatpage),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
