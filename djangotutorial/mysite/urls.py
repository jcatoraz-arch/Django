from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from polls.views import portfolio, blog
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("blog/", include("blog.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#esto permite que django pueda mostrar las imagenes que guardemos en la carpeta media mientras estoy desarrollando

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns