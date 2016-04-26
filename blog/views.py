
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Notice
from .forms import PostForm, CommentForm, NoticeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def notice_list(request):
    notices = Notice.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    public = Notice.objects.filter(privacy="Public").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blog/notice_list.html',{'notices': notices, 'public': public})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'blog/notice_detail.html', {'notice': notice})



@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@staff_member_required
def notice_new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.published_date = timezone.now()
            notice.save()
            return redirect('blog.views.notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'blog/notice_edit.html', {'form': form})

@staff_member_required
def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('blog.views.notice_detail', pk=notice.pk)
    else:
        form = NoticeForm(instance=post)
    return render(request, 'blog/notice_edit.html', {'form': form})

# @login_required
# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     return render(request, 'blog/post_draft_list.html', {'posts': posts})

# @login_required
# def post_publish(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('blog.views.post_detail', pk=pk)

# @login_required
# def publish(self):
#     self.published_date = timezone.now()
#     self.save()

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@staff_member_required
def notice_remove(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('blog.views.notice_list')

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()

#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)
