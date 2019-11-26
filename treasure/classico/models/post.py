from classico.models.base import *
from django.contrib.auth.models import User
from .link import Link
from .arquivo import Arquivo
from .comentario import Comentario

class Post(BaseModel):
	"""docstring for Post"""
	TIPO_CHOICES = (
        ("MC", "Música"),
        ("VD", "Vídeo"),
        ("QT", "Questões"),
        ("LV", "Livros"),
    )
	tipo = models.CharField(max_length= 50, choices=TIPO_CHOICES, blank = False, null = False)
	img_principal = models.ImageField(upload_to= 'classico/', blank = True, null = True)
	titulo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=1000)
	
	# def __init__(self, arg):
	# 	super(Post, self).__init__()
	# 	self.arg = arg
	# 	
	