# Generated by Django 5.1.2 on 2024-10-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_gerenciarreceita_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gerenciarreceita',
            options={},
        ),
        migrations.RemoveField(
            model_name='gerenciarreceita',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='gerenciarreceita',
            name='img',
        ),
        migrations.AddField(
            model_name='gerenciarreceita',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='receitas/'),
        ),
        migrations.AddField(
            model_name='gerenciarreceita',
            name='ingredientes',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gerenciarreceita',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gerenciarreceita',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]