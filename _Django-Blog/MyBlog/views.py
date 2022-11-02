from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.order_by('-id')

    return render(request, 'MyBlog/index.html', {
        'posts': posts
    })


def noticia(request, post_id):
    postagem = get_object_or_404(Post, id=post_id)

    return render(request, 'MyBlog/noticia_id.html', {
        'postagem': postagem
    })


def selecao(request):
    selecao = Post.objects.filter(
        category='11'
    )

    return render(request, 'MyBlog/selecao.html', {
        'selecao': selecao
    })


def brasileirao(request):
    brasileirao = Post.objects.filter(
        category='12'
    )

    return render(request, 'MyBlog/brasileirao.html', {
        'brasileirao': brasileirao
    })


def sobre(request):
    posts = Post.objects.order_by('-id')

    return render(request, 'MyBlog/sobre.html', {
        'posts': posts
    })