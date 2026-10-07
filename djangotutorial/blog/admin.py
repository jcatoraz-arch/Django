from django.contrib import admin
from .models import Post, Comentario

admin.site.register(Post)
# con esto me aparece la opcion para agregar un comentario en la seccion de admin
admin.site.register(Comentario)
#ahora con esto en admin puedo crear post y comentarios desde Django
