from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
    
def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogs/show.html', {'post': post})

def destroy(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts')

def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    return render(request, 'blogs/edit.html', {'form': form, 'post': post})

def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('posts')
    else:
        return render(request, 'blogs/edit.html', {'form': form, 'post': post})
