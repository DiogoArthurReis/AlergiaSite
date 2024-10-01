from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(GerenciarUsuario)
admin.site.register(GerenciarVivencia)
admin.site.register(GerenciarComentario)
admin.site.register(GerenciarCategoria)
admin.site.register(GerenciarProduto)
admin.site.register(GerenciarReceita)
admin.site.register(GerenciarPagina_Inicial)