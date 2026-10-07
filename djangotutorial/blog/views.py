from django.shortcuts import render
from django.shortcuts import render
from .models import Post


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha")
    return render(request, "blog/lista_posts.html", {"posts": posts})
# bussca todos los posts y los ordena del mas nuevo al mas viejo
def detalle_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "blog/detalle_post.html", {"post": post})
# django busca el post por el id