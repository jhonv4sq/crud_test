from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/index.html', {'posts': posts})

def show(request, id):
    post = get_object_or_404(Post, id=id)
    
    context = {
        'post': post
    }

    return render(request, 'blogs/show.html', context)

@login_required
def create(request):
    form = PostForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'blogs/create.html', context)
    
@login_required
def store(request):
    form = PostForm(request.POST)
    
    context = {
        'form': form
    }
    
    if form.is_valid():
        post = form.save(commit=False)  # Crea una instancia del modelo Post pero no la guarda en la base de datos
        post.user_id = request.user.id  # Asigna el usuario logueado como autor del post
        post.save()  # Ahora guarda el post en la base de datos, con el autor asignado
        return redirect('posts')
    else:
        return render(request, 'blogs/create.html', context)

@login_required
def destroy(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts')

@login_required
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post
    }
    
    return render(request, 'blogs/edit.html', context)

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST, instance=post)
    
    context = {
        'form': form,
        'post': post
    }
    
    if form.is_valid():
        form.save()
        return redirect('posts')
    else:
        return render(request, 'blogs/edit.html', context)
