from django.contrib import admin
from django.urls import path
from . import views
from data.views import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("data/", data)
]
