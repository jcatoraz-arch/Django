from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.lista_posts, name="lista_posts"),
    path("<int:post_id>/", views.detalle_post, name="detalle_post"),
]
# define la direccion que va a mostrar nuestro listado de posts