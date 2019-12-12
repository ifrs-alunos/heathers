from django.shortcuts import render
from .models import *

def index(request):
	publicacao_recente_lista = Noticia.objects.order_by('-id')
	
	dados = {
		'publicacao_recente_lista': publicacao_recente_lista,
	}

	return render(request, 'core/index.html', dados)

def obras(request):
	return render(request, 'core/services.html')

def questoes(request):
	publicacao_recente_lista = Questao.objects.order_by('-id')
	
	dados = {
		'publicacao_recente_lista': publicacao_recente_lista,
	}

	return render(request, 'core/about.html', dados)

'''def comentarios(request):
	publicacao = Comentario.objects.order_by('-id')
	form = ComentarioForm()
	
	dados = {
		'publicacao': publicacao,
		'form': form,
	}

	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		else:
			form = ComentarioForm()

		return render(request, 'core/comentario.html', {'form': form})
	
	return render(request, 'core/comentario.html', dados)
'''

def sobre(request):
	return render(request, 'core/sobre.html')

def midias(request):
	return render(request, 'core/portfolio.html')
