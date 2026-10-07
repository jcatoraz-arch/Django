from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha")
    likes = request.session.get("likes", [])

    return render(request, "blog/lista_posts.html", {
        "posts": posts,
        "likes": likes
    })


def filtrar_categoria(request, categoria):
    posts = Post.objects.filter(categoria=categoria).order_by("-fecha")
    likes = request.session.get("likes", [])

    return render(request, "blog/lista_posts.html", {
        "posts": posts,
        "likes": likes
    })


def ordenar_posts(request, orden):
    if orden == "viejo":
        posts = Post.objects.all().order_by("fecha")
    else:
        posts = Post.objects.all().order_by("-fecha")

    likes = request.session.get("likes", [])

    return render(request, "blog/lista_posts.html", {
        "posts": posts,
        "likes": likes
    })


def dar_like(request, post_id):
    post = Post.objects.get(id=post_id)

    likes = request.session.get("likes", [])

    if post_id in likes:
        likes.remove(post_id)
        post.likes -= 1
    else:
        likes.append(post_id)
        post.likes += 1

    request.session["likes"] = likes
    post.save()

    return render(request, "blog/lista_posts.html", {
        "posts": Post.objects.all().order_by("-fecha"),
        "likes": likes
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
def eliminar_comentario(request, comentario_id):
    if not request.user.is_staff:
        return redirect("blog:lista_posts")

    comentario = get_object_or_404(Comentario, id=comentario_id)
    post_id = comentario.post.id

    comentario.delete()

    return redirect("blog:detalle_post", post_id=post_id)
# django busca el post por el id y busca los comentarios pertenecientes a ese post y se los pasa al HTML
# cuando alguien manda el formulario, crea automaticamente un comentario asociado al post