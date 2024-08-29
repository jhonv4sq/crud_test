from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings

def hello_world(request):
    
    return HttpResponse('Hello world')

def index(request):
    
    context = {'greeting': 'Hello World!'}
    
    return render(request, 'index.html', context)

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)