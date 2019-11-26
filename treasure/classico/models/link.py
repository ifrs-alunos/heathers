from classico.models.base import BaseModel
from classico.models import post
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
	"""docstring for Link"""
	"""Variável url recebem o endereço de música ou vídeo conforme o tipo escolhido"""
	url = models.CharField(max_length=1000)

	# def __init__(self, arg):
	# 	super(Link, self).__init__()
	# 	self.arg = arg
