from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Livro, Cidade, Autor, Editora, Leitor, Genero, Reserva

# ----------------------------
# Views de página principal
# ----------------------------
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# ----------------------------
# Views de livros
# ----------------------------
class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})
    
    def post(self, request, *args, **kwargs):
        # Aqui você pode tratar submissão de formulário, se necessário
        pass

class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        # Busca o livro pelo ID ou retorna 404 se não existir
        livro = get_object_or_404(Livro, id=id)
        # Exclui o livro
        livro.delete()
        # Adiciona uma mensagem de sucesso
        messages.success(request, 'Livro excluído com sucesso!')
        # Redireciona para a lista de livros
        return redirect('livros')

# ----------------------------
# Views de reservas
# ----------------------------
class ReservaView(View):
    def get(self, request, *args, **kwargs):
        reservas = Reserva.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})

# ----------------------------
# Views de cadastro de entidades
# ----------------------------
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})