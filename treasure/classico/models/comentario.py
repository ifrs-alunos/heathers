from classico.models.base import BaseModel
from classico.models import post
from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
	"""docstring for Comentário"""
	TIPO_CHOICES = (
		("DU", "Dúvida"),
		("CO", "Comentário"),
	)

	tipo = models.CharField(max_length= 200, choices =TIPO_CHOICES, blank=False, null=False)
	descreva = models.CharField(max_length=240)
