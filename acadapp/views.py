from django.shortcuts import render, redirect
from login.models import *


def index(request):

    if request.user.is_authenticated:
        context = {
            'name':request.user.username,
            'college':Profile.objects.get(user=request.user).college.replace(" ", ""),
        }
    else:
        context={}

    return render(request, 'index.html', context)