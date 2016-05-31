from django.contrib import admin
from .models import AboutUs, Gallery
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'photo', 'text']
    list_display = ('title','category',)


class GalleryAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'photo', 'text']
    list_display = ('title','category',)


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Gallery, GalleryAdmin)

