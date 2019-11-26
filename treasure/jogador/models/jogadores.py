from jogador.models.base  import BaseModel
from django.contrib.auth.models import User
from django.db import models
from .times import Time

class Jogador(models.Model):
	"""classe jogador"""
	nome = models.CharField(max_length = 200)
	apelido = models.CharField(max_length = 200)
	data_nascimento = models.DateField()
	numero = models.IntegerField()
	posicao = models.CharField(max_length = 200)
	qualidade = models.IntegerField()
	cartoes = models.IntegerField()
	suspenso = models.CharField(max_length=200)
	time = models.ForeignKey(Time, models.SET_NULL, null=True, related_name='platel')
	
	# def verificar_condicao(self):
	# 	a = input("Digite a quantidade de cartões:\n\n" )
	# 	if self.cartoes > 2:
	# 		self.suspenso = True
	# 		f = "SUSPENSO"
	# 		print(f)
	# 	else:
	# 		g = "TA PRA JOGO"		
	# 		print(g) 
	
	def __str__(self):
		return ("{}: {} - {} ({})  - {} CONDIÇÃO: {}".format(self.posicao, self.numero, self.nome, self.apelido, self.data_nascimento, self.suspenso))
