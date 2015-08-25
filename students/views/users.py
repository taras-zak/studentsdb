from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User


def ProfilesView(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html',
        {'users': users})

def ProfileView(request, uid):
    user_profile = User.objects.get(id = uid)
    return render(request, 'users/user_profile.html',
        {'user_profile': user_profile})
