from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, 
    LivrosView, 
    ReservaView, 
    CidadesView, 
    AutoresView, 
    EditorasView, 
    LeitoresView, 
    GenerosView, 
    DeleteLivroView
)

urlpatterns = [
    # Administração
    path('admin/', admin.site.urls),

    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # Livros
    path('livros/', LivrosView.as_view(), name='livros'),
    path('delete/<int:id>/', DeleteLivroView.as_view(), name='delete'),

    # Reservas
    path('reserva/', ReservaView.as_view(), name='reserva'),

    # Cidades
    path('cidade/', CidadesView.as_view(), name='cidade'),

    # Autores
    path('autor/', AutoresView.as_view(), name='autor'),

    # Editoras
    path('editor/', EditorasView.as_view(), name='editora'),

    # Leitores
    path('leitor/', LeitoresView.as_view(), name='leitor'),

    # Gêneros
    path('genero/', GenerosView.as_view(), name='genero'),
]