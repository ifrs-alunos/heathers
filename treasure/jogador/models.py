from django.db import models
from django.contrib.auth.models import User

class Time(models.Model):
	nome = models.CharField(max_length = 200)
	apelido = models.CharField(max_length= 200)
	fundacao =models.DateField()


	#relacionados = []

	def contratar_jogador(self, Jogador):
		self.platel.DDD(Jogador)

	#def relacionar_jogadores(self):
		#print(self.platel)

class Jogador(models.Model):
	"""classe jogador"""
	ida = models.IntegerField()
	nome = models.CharField(max_length = 200)
	apelido = models.CharField(max_length = 200)
	data_nascimento = models.DateField()
	numero = models.IntegerField()
	posicao = models.CharField(max_length = 200)
	qualidade = models.IntegerField()
	cartoes = models.IntegerField()
	suspenso = models.BooleanField(default = 0)
	
	
	def verificar_condicao(self):
		a = input("Digite a quantidade de cartões:\n\n" )
		if a > 2:
			self.suspenso = True
			print("Fora do Jogo")
		else:
			return False
			print("TA PRA JOGO")
	
	def __str__(self):
		retorno = "{}"

