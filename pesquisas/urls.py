from django.urls import path
from . import views

urlpatterns = [
    path("", views.pesquisas, name="pesquisas"),
    path("<str:pesquisa_id>/", views.pesquisa)
]
