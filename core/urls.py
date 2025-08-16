from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("create/", views.create),
    path("results/", views.results),
    path("auth/", include("authentication.urls")),
    path("pesquisas/", include("pesquisas.urls")),
    path("api/", include("api.urls"))
]
