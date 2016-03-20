from django.contrib import admin
from .models import Post, Comment, Notice
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class MCEFlatPageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        exclude = []

class MCEFlatPageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = MCEFlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MCEFlatPageAdmin)



class NoticeAdmin(admin.ModelAdmin):
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
