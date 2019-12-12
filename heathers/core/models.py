from django.db import models

class Noticia(models.Model):
	titulo = models.CharField(max_length=200)
	subtitulo = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	image = models.ImageField(upload_to='media/', null=True)

	def __str__(self):
		return self.titulo

class Midia(models.Model):
	link = models.CharField(max_length=200)

	def __str__(self):
		return self.link

class Questao(models.Model):
	titulo = models.CharField(max_length=200)
	subtitulo = models.CharField(max_length=200)
	file = models.FileField(upload_to='media/')

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	nome = models.CharField(max_length=100)
	texto = models.CharField(max_length=200)
