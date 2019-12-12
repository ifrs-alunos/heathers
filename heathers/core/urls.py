from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.index),
	path('obras/', views.obras, name='obras'),
	path('midias/', views.midias, name='midias'),
	#path('comentarios/', views.comentarios, name='comentarios'),
	path('sobre/', views.sobre, name='sobre'),
	path('questoes/', views.questoes, name='questoes'),
]
