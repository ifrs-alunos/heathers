from classico.models.base import BaseModel
from classico.models import post
from django.contrib.auth.models import User
from django.db import models

class Arquivo(models.Model):
	"""docstring for Arquivo"""
	arquivo = models.CharField(max_length=1000, help_text='Adicione apenas o endereço do seu pdf')
	# def __init__(self, arg):
	# 	super(Arquivo,model).__init__()
	# 	self.arg = arg
