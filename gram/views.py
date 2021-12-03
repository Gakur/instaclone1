from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# profile page
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    posts = Post.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"posts": posts, "profile": profile})
