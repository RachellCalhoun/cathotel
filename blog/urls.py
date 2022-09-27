from django.urls import  re_path
from . import views

urlpatterns = [
    re_path(r'^qna$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^notices/$', views.notice_list, name='notice_list'),
    re_path(r'^notice/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    re_path(r'^notice/(?P<pk>[0-9]+)/edit/$', views.notice_edit, name='notice_edit'),
    re_path(r'^notice/new/$', views.notice_new, name='notice_new'),
    # re_path(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    # re_path(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # re_path(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]

app_name = 'blog'