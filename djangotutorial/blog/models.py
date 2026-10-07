from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to="posts/", blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    #esto basicamente es que cada comentario queda relacionado con un post, tiene nombre, texto y fecha, etc
