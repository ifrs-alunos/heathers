# Generated by Django 2.2.6 on 2019-10-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classico', '0004_auto_20191003_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.CharField(default=1, help_text='Somente se sor Musicas', max_length=800),
            preserve_default=False,
        ),
    ]
