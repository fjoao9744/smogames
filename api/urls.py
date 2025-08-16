from django.urls import path
from api.views import RespostasAPI

urlpatterns = [
    path("", RespostasAPI.as_view()),
    path("<int:pesquisa_id>/", RespostasAPI.as_view())
]
