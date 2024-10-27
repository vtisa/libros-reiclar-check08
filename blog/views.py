from django.shortcuts import render, get_object_or_404
from .models import Entrada, Autor

# Create your views here.
def lista_entradas(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    entradas = Entrada.objects.filter(autor_id=autor_id)
    return render(request, 'blog/lista_entradas.html', {'autor': autor, 'entradas': entradas})


def index(request):
    autores = Autor.objects.all()
    return render(request, 'blog/index.html', {'autores': autores})
