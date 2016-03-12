from django import forms

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

	class Meta:
		model = Notice
		fields = ("title", "text", "img", )
