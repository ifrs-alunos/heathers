# Generated by Django 2.1.7 on 2019-09-18 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0003_auto_20190918_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='ida',
        ),
    ]
