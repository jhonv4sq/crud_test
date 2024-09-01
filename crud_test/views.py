from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, views as auth_views
from django.conf import settings
from .forms import CustomAuthenticationForm, UserRegisterForm
from .decorators import unauthenticated_user

def hello_world(request):
    
    return HttpResponse('Hello world')

def index(request):
    
    context = {'greeting': 'Hello World!'}
    
    return render(request, 'index.html', context)

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

@unauthenticated_user
def login_user(request):
    template = 'auth/login.html'
    view = auth_views.LoginView.as_view(template_name=template, authentication_form=CustomAuthenticationForm)
    return view(request)

@unauthenticated_user
def register_user_view(request):
    form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

@unauthenticated_user
def register_user(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, 'auth/register.html', {'form': form})
        