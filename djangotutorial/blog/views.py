from django.shortcuts import render
from .models import Post, Comentario


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha")
    return render(request, "blog/lista_posts.html", {"posts": posts})

def filtrar_categoria(request, categoria):
    posts = Post.objects.filter(categoria=categoria).order_by("-fecha")

    return render(request, "blog/lista_posts.html", {
        "posts": posts
    })

def ordenar_posts(request, orden):
    if orden == "viejo":
        posts = Post.objects.all().order_by("fecha")
    else:
        posts = Post.objects.all().order_by("-fecha")

    return render(request, "blog/lista_posts.html", {
        "posts": posts
    })

def detalle_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        nombre = request.POST["nombre"]
        texto = request.POST["texto"]

        Comentario.objects.create(
            post=post,
            nombre=nombre,
            texto=texto
        )

    comentarios = Comentario.objects.filter(post=post).order_by("-fecha")

    return render(request, "blog/detalle_post.html", {
        "post": post,
        "comentarios": comentarios
    })
def dar_like(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()

    return render(request, "blog/lista_posts.html", {
        "posts": Post.objects.all().order_by("-fecha")
    })
# django busca el post por el id y busca los comentarios pertenecientes a ese post y se los pasa al HTML
# cuando alguien manda el formulario, crea automaticamente un comentario asociado al post