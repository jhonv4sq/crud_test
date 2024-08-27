from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    
    return HttpResponse('Hello world')

def index(request):
    
    context = {'greeting': 'Hello World!'}
    
    return render(request, 'index.html', context)