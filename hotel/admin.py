from django.contrib import admin
from .models import AboutUs, CatGallery, HotelGallery
# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'photo', 'text']
    list_display = ('title','category')

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(CatGallery)
admin.site.register(HotelGallery)

