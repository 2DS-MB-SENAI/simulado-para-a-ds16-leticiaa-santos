from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros' : livros})

@api_view(['GET'])
def read_livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return Response(serializer.data)