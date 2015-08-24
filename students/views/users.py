from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User

def ProfileView(request, uid):
    user_profile = User.objects.get(id = uid)
    return render(request, 'registration/user_profile.html',
        {'user_profile': user_profile})
