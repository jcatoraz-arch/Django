# portfolio personal joaquin catoraz - django

es mi sitio web personal desarrollado con django. el proyecto incluye un portfolio y un blog con publicaciones, imagenes y comentarios.

## funcionalidades

 el trabajo incluye un portfolio personal que habla sobre mis cualidades y mis proyectos, un blog integrado, publicaciones que estan ordenadas por fecha e incluye imagenes, vos podes comentar estas publicaciones si asi lo deseas. ademas tiene un panel de admin de django en el cual podes eliminar y agregar post, comentarios, etc y tenes una libre navegacion entre el portfolio y mi blog

## tecnologias que utilice

* python
* django
* html
* css
* sqlite
* bootstrap

## estructura principal

* blog/: aplicacion encargada del blog y los comentarios
* polls/: aplicacion utilizada durante el tutorial de django
* mysite/: configuracion principal del proyecto
* templates/: templates del sitio
* static/: archivos estaticos
* media/: imagenes subidas a las publicaciones
* manage.py: archivo principal para ejecutar comandos de django
* db.sqlite3: base de datos del proyecto

## como ejecutar el proyecto

primer paso: abrir una terminal en la carpeta `djangotutorial`
segundo paso: ejecutar:

```bash
python manage.py runserver
```

3. abrir en el navegador:

```text
http://127.0.0.1:8000/
```

el portfolio se encuentra en la pagina principal y el blog en:

```text
http://127.0.0.1:8000/blog/
```

## administracion

para acceder al panel de administracion:

```text
http://127.0.0.1:8000/admin/
```

desde el administrador se pueden gestionar las publicaciones y los comentarios

si el profe necesita mi contraseña y usuario se lo dejo aca:

* contraseña: Indio0910
* usuario: joakto
