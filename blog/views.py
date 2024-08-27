from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/index.html', {'posts': posts})

def create(request):
    return render(request, 'blogs/create.html')
    
# def store(request):
#     return ''

# def edit(request):
#     return ''

# def update(request):
#     return ''

# def destroy(request):
#     return ''
