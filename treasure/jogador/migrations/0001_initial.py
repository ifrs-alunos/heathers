# Generated by Django 2.1.7 on 2019-09-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ida', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('numero', models.IntegerField()),
                ('posicao', models.CharField(max_length=200)),
                ('qualidade', models.IntegerField()),
                ('cartoes', models.IntegerField()),
                ('suspenso', models.BooleanField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
