from django.contrib import admin
from .models import Post, Comment, Notice

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notice)
# Register your models here.
