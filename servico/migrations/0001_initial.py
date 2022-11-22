# Generated by Django 4.1.2 on 2022-11-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço do serviço', max_digits=5, verbose_name='Preço')),
                ('descricao', models.TextField(help_text='Descrição e observações de serviços', max_length=300, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
