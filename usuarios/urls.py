from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', view=views.criar_usuario, name='criar_usuario'),
    path('auth/login/', view=views.logar_usuario, name='logar_usuario')
]