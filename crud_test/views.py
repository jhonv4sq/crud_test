from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, views as auth_views
from django.conf import settings
from .forms import CustomAuthenticationForm
from .decorators import unauthenticated_user

def hello_world(request):
    
    return HttpResponse('Hello world')

def index(request):
    
    context = {'greeting': 'Hello World!'}
    
    return render(request, 'index.html', context)

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def login_user(request):
    template = 'auth/login.html'
    view = auth_views.LoginView.as_view(template_name=template, authentication_form=CustomAuthenticationForm)
    decorated_view = unauthenticated_user(view)
    return decorated_view(request)