from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/index.html', {'posts': posts})

@login_required
def create(request):
    form = PostForm()
    return render(request, 'blogs/create.html', {'form': form})
    
@login_required
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

@login_required
def destroy(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts')

@login_required
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    return render(request, 'blogs/edit.html', {'form': form, 'post': post})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('posts')
    else:
        return render(request, 'blogs/edit.html', {'form': form, 'post': post})
