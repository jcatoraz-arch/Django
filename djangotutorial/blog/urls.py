from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.lista_posts, name="lista_posts"),
    path("categoria/<str:categoria>/", views.filtrar_categoria, name="filtrar_categoria"),
    path("ordenar/<str:orden>/", views.ordenar_posts, name="ordenar_posts"),
    path("<int:post_id>/", views.detalle_post, name="detalle_post"),
    path("like/<int:post_id>/", views.dar_like, name="dar_like"),
    path("comentario/<int:comentario_id>/eliminar/", views.eliminar_comentario, name="eliminar_comentario"),
]
# define la direccion que va a mostrar nuestro listado de posts