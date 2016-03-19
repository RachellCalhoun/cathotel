from django.contrib import admin
from .models import Post, Comment, Notice

from django_markdown.admin import AdminMarkdownWidget


class NoticeAdmin(admin.ModelAdmin):
    formfield_overrides = {'text': {'widget': AdminMarkdownWidget}}
    fields = ['author', 'privacy', 'title', 'img', 'text', 'published_date']
    list_display = ('title','privacy', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title','text']

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'img', 'text', 'published_date']
    list_display = ('title','author', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title', 'text','author']

class CommentAdmin(admin.ModelAdmin):
	# author = request.user
    fields = ['author', 'post', 'text']
    list_display = ('text', 'author', 'post', 'created_date' )
    list_filter = ['created_date', 'author']
    search_fields = ['post','author', 'text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notice, NoticeAdmin)
# Register your models here.
