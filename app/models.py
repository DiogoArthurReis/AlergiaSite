from django.db import models

# Create your models here.

class GerenciarUsuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "GerenciarUsuario"

    def __str__(self):
        return f'{self.nome} {self.email}'
        
class GerenciarVivencia(models.Model):
    titulo = models.CharField(max_length=100) 
    img = models.ImageField() 
    descricao = models.CharField(max_length=100) 

    class Meta:
        verbose_name_plural = "GerenciarVivencia"

    def __str__(self):
        return f'{self.titulo} {self.img} {self.descricao}'
        
class GerenciarComentario(models.Model):
    usuario = models.ForeignKey(GerenciarUsuario, on_delete=models.CASCADE) 
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario.nome} em {self.data.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name_plural = "GerenciarComentario"

    def __str__(self):
        return f'{self.mensagem}'
        
class GerenciarProduto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    img = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} ({self.categoria})'
        
class GerenciarReceita(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100) 
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