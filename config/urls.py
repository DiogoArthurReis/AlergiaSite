"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='pagina_inicial.html'), name='index'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('vivencia.html', VivenciaView.as_view(), name='vivencia'),
    path('comentario/', ComentarioView.as_view(), name='comentario'),
    path('categoria/', CategoriaView.as_view(), name='categoria'),
    path('produto.html', ProdutoView.as_view(), name='produto'),
    path('receita.html', ReceitaView.as_view(), name='receita'),
    path('pagina_inicial.html', Pagina_InicialView.as_view(), name='pagina_inicial'),
]

