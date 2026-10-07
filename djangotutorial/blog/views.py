from django.shortcuts import render
from django.shortcuts import render
from .models import Post, Comentario


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha")
    return render(request, "blog/lista_posts.html", {"posts": posts})
# bussca todos los posts y los ordena del mas nuevo al mas viejo
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
# django busca el post por el id y busca los comentarios pertenecientes a ese post y se los pasa al HTML
# cuando alguien manda el formulario, crea automaticamente un comentario asociado al post