from django.contrib import admin
from .models import AboutUs, CatGallery, HotelGallery
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'photo', 'text']
    list_display = ('title','category',)

class CatGalleryAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'photo', 'text']
    list_display = ('title','category',)

class HotelGalleryAdmin(admin.ModelAdmin):
    fields = ['category', 'privacy', 'title', 'photo', 'text']
    list_display = ('title','category','privacy',)


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(CatGallery, CatGalleryAdmin)
admin.site.register(HotelGallery, HotelGalleryAdmin)

