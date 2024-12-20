# Generated by Django 5.1.2 on 2024-10-29 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_gerenciarcomentario_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gerenciarcomentario',
            options={'verbose_name_plural': 'GerenciarComentario'},
        ),
        migrations.AlterModelOptions(
            name='gerenciarpagina_inicial',
            options={'verbose_name_plural': 'GerenciarPagina_Inicial'},
        ),
        migrations.AlterModelOptions(
            name='gerenciarusuario',
            options={'verbose_name_plural': 'GerenciarUsuario'},
        ),
        migrations.AlterModelOptions(
            name='gerenciarvivencia',
            options={'verbose_name_plural': 'GerenciarVivencia'},
        ),
        migrations.RemoveField(
            model_name='gerenciarcomentario',
            name='nome',
        ),
        migrations.AlterField(
            model_name='gerenciarcomentario',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_email', to='app.gerenciarusuario'),
        ),
        migrations.AlterField(
            model_name='gerenciarproduto',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gerenciarvivencia',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gerenciarvivencia',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
