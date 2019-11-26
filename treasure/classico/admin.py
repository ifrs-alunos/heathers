from django.contrib import admin
#aqui sei importa classe 
from .models import Post
from .models import Link
from .models import Arquivo
from .models import Comentario

# Registra o modulo da classe
admin.site.register(Post)
admin.site.register(Link)
admin.site.register(Arquivo)
admin.site.register(Comentario)
