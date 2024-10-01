from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pagina_inicial.html')
    def post(self, request):
        pass

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = GerenciarUsuario.objects.all()
        return render(request, 'Usuario.html', {'Usuarios': usuarios})
    
class VivenciaView(View):
    def get(self, request, *args, **kwargs):
        vivencias = GerenciarVivencia.objects.all()
        return render(request, 'Vivencia.html', {'vivencias': vivencias})

class ComentarioView(View):
    def get(self, request, *args, **kwargs):
        comentarios = GerenciarComentario.objects.all()
        return render(request, 'Comentario.html', {'comentarios': comentarios})
    
class CategoriaView(View):
    def get(self, request, *args, **kwargs):
        categorias = GerenciarCategoria.objects.all()
        return render(request, 'Categoria.html', {'categorias': categorias})
    
class ProdutoView(View):
    def get(self, request, *args, **kwargs):
        produtos = GerenciarProduto.objects.all()
        return render(request, 'Produto.html', {'produtos': produtos})
    
class ReceitaView(View):
    def get(self, request, *args, **kwargs):
        receitas = GerenciarReceita.objects.all()
        return render(request, 'Receita.html', {'receitas': receitas})
    
class Pagina_InicialView(View):
    def get(self, request, *args, **kwargs):
        pagina_inicial = GerenciarPagina_Inicial.objects.all()
        return render(request, 'Pagina_Inicial.html', {'pagina_inicial': pagina_inicial})
