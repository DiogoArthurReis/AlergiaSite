# Generated by Django 5.1.2 on 2024-10-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_gerenciarpagina_inicial_detalhamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerenciarreceita',
            name='ingredientes',
            field=models.TextField(),
        ),
    ]
