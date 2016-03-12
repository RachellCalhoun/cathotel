from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserCreateForm, UserEditForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
# from .models import UserProfile
# from crafts.models import CraftPost
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            # userprofile = UserProfile(user=user)
            # userprofile.save()
            login(request, user)
            messages.add_message(request, messages.INFO, 'Thank you for registering!', 'message register-success')
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', { 'form': form })

# def register(request):
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = request.POST['username']
#             password = request.POST['password1']
#             user = authenticate(username=username, password=password)
#             user.backend = "django.contrib.auth.backends.ModelBackend"
#             if 'picture' in request.FILES:
#                 picture=request.FILES['picture']
#             else:
#                 picture = None
#             userprofile = UserProfile(user=user, location=request.POST['location'], picture=picture, hobby=request.POST["hobby"])
#             userprofile.save()
#             login(request, user)
#             messages.add_message(request, messages.INFO, 'Thank you for registering!', 'message register-success')
#             return HttpResponseRedirect('/')
#     else:
#         form = UserCreateForm()
#     return render(request, 'registration/register.html', { 'form': form })
