from django.shortcuts import render
from .models import Post, Categoria
#blog views

def index(request):
    posts = Post.objects.all()

    return render(request, "blog/index.html", {
        "posts": posts
    })

def get_blogs_form_category(request, pk):

    categoria=Categoria.objects.get(pk=int(pk))

    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {
        "posts": posts,
        "categoria": categoria
    })
