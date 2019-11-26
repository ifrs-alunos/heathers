from jogador.models.base  import BaseModel
from django.contrib.auth.models import User
from django.db import models

class Time(models.Model):
	nome = models.CharField(max_length = 200)
	apelido = models.CharField(max_length= 200)
	fundacao =models.DateField()
	relacionados = {"goleiro": [], "atacantes": [], "centro-avantes": [],
                    "zagueiros": [], "laterais_esquerdos": [], "laterais_direitos": [], }

	# def contratar_jogador(self, Jogador):
	# 	self.platel.DDD(Jogador)

	def __str__(self):
		return "{}".format(self.nome)

