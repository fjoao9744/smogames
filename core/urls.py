from django.contrib import admin
from django.urls import path, include
from . import views
from data.views import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("create/", views.create),
    path("data/", data),
    path("auth/", include("authentication.urls")),
    path("pesquisas/", include("pesquisas.urls"))
]
