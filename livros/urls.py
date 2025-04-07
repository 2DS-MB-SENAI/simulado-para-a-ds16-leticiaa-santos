from django.urls import path
from . import views

urlpatterns = [
    path('livros/', view=views.listar_livros, name='listar_livros'),
    path('api/livros/', view=views.read_livros),
]