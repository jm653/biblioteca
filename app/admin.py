from django.contrib import admin
from .models import *

# INLINE: Livro dentro de Autor
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1


# ADMIN DO AUTOR
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]


# REGISTROS
admin.site.register(Cidade)
admin.site.register(Autor, AutorAdmin)  # <- IMPORTANTE
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(Reserva)