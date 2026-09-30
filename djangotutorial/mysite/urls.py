from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from polls.views import portfolio, blog

urlpatterns = [
    path("", portfolio, name="portfolio"),
    path("blog/", blog, name="blog"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns