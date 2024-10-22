from django import forms
from .models import GerenciarComentario  

class GerenciarComentarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = GerenciarComentario
        fields = ['mensagem']  
