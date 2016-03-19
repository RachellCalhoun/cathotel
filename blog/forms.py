from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget
from .models import Post, Comment, Notice


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)

class NoticeForm(forms.ModelForm):
	text = forms.CharField(widget=MarkdownWidget())

	class Meta:
		model = Notice
		fields = ("title", "text", "img", )
