from django.db import models

# Create your models here.

class GerenciarUsuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "GerenciarUsuario"

    def __str__(self):
        return f'{self.nome} {self.email} {self.telefone} {self.senha}'
        
class GerenciarVivencia(models.Model):
    titulo = models.CharField(max_length=100) 
    img = models.ImageField() 
    descricao = models.CharField(max_length=100) 

    class Meta:
        verbose_name_plural = "GerenciarVivencia"

    def __str__(self):
        return f'{self.titulo} {self.img} {self.descricao}'
        
class GerenciarComentario(models.Model):
    mensagem = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "GerenciarComentario"

    def __str__(self):
        return f'{self.mensagem}'
        
class GerenciarCategoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "GerenciarCategoria"

    def __str__(self):
        return f'{self.nome}'
        
class GerenciarProduto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(GerenciarCategoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    img = models.ImageField()

    class Meta:
        verbose_name_plural = "GerenciarProduto"

    def __str__(self):
        return f'{self.nome} {self.categoria} {self.descricao} {self.img}'
        
class GerenciarReceita(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(GerenciarCategoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    img = models.ImageField()

    class Meta:
        verbose_name_plural = "GerenciarReceita"

    def __str__(self):
        return f'{self.nome} {self.categoria} {self.descricao} {self.img}'
    

class GerenciarPagina_Inicial(models.Model):
    detalhamento = models.CharField(max_length=1000)
    sintomas = models.CharField(max_length=1000)
    tratamentos = models.CharField(max_length=1000)
    nome_alergia = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "GerenciarPagina_Inicial"

    def __str__(self):
        return f'{self.detalhamento} {self.sintomas} {self.tratamentos} {self.nome_alergia}'