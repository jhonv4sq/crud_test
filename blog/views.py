from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/index.html', {'posts': posts})

def create(request):
    form = PostForm()
    return render(request, 'blogs/create.html', {'form': form})
    
def store(request):
    form = PostForm(request.POST)
    
    if form.is_valid():
        form.save()    
        return redirect('posts')
    else:
        return render(request, 'blogs/create.html', {'form': form})

# def edit(request):
#     return ''

# def update(request):
#     return ''

# def destroy(request):
#     return ''
