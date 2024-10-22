from django.views import View
from .models import *
from django.shortcuts import render, redirect
from .forms import GerenciarComentarioForm
from django.contrib.admin.views.decorators import staff_member_required


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
    def get(self, request):
        form = GerenciarComentarioForm()
        mensagens = GerenciarComentario.objects.all()
        return render(request, 'comentario.html', {'form': form, 'mensagens': mensagens})

    def post(self, request):
        form = GerenciarComentarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']

            # Verificar se o usuário já existe ou criar um novo
            usuario, created = GerenciarUsuario.objects.get_or_create(email=email, defaults={'nome': nome})

            # Criar a mensagem
            mensagem = GerenciarComentario(usuario=usuario, mensagem=form.cleaned_data['mensagem'])
            mensagem.save()

            return redirect('comentario')  # Redireciona para a mesma página após salvar

        mensagens = GerenciarComentario.objects.all()
        return render(request, 'comentario.html', {'form': form, 'mensagens': mensagens})
    
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
    
