from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def hello_world(request):
    
    return HttpResponse('Hello world')

def index(request):
    
    context = {'greeting': 'Hello World!'}
    
    return render(request, 'index.html', context)