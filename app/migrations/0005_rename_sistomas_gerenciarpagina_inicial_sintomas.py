# Generated by Django 5.0.7 on 2024-10-01 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_gerenciarcategoria_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gerenciarpagina_inicial',
            old_name='sistomas',
            new_name='sintomas',
        ),
    ]