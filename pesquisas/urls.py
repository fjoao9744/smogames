from django.urls import path
from . import views

urlpatterns = [
    path("", views.pesquisas, name="pesquisas"),
    path("pesquisa/<str:pesquisa_id>", views.pesquisa)
    
]
