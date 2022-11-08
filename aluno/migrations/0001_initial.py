# Generated by Django 4.1.3 on 2022-11-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=150)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=150)),
                ('curso', models.CharField(choices=[('Apicultura', 'Apicultura'), ('Alimentos', 'Alimentos'), ('Informática', 'Informática')], max_length=150)),
            ],
        ),
    ]