# Generated by Django 4.2.2 on 2023-06-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='data_criacao',
            field=models.DateField(verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
    ]
