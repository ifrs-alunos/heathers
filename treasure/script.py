import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treasure.settings')
django.setup()

from jogador.models.jogadores import Jogador
from jogador.models.times import Time
import datetime 

jogador = Jogador.objects.all()


time1 = Time(1, 'Grêmio', 'G', datetime.date(1903, 9, 15))
time1.save()

#Criando os jogadores do primeiro time com seus devidos dados
jogador0 = Jogador(1, "Mateus", "te", datetime.date(2000, 2, 4), 3, "goleiro", 1, 2, "SUSPENSO", time1.id)
jogador2 = Jogador(2, "João", "jao", datetime.date(1999, 7, 9), 5, "zagueiro", 1, 0, "TÁ PRA JOGO", time1.id)
jogador5 = Jogador(5, "Diego", "di", datetime.date(1999, 7, 9), 1, "meio", 1, 2, "SUSPENSO", time1.id)
jogador6 = Jogador(6, "Eduardo", "Edu", datetime.date(1999, 7, 9), 9, "zagueiro", 1, 0, "TÁ PRA JOGO", time1.id)
jogador7 = Jogador(7, "Luis Eduardo", "Duds", datetime.date(1999, 7, 9), 30, "meio", 1, 2, "SUSPENSO", time1.id)
jogador8 = Jogador(8, "Isac", "zac", datetime.date(1999, 7, 9), 11, "atacante", 1, 2, "SUSPENSO", time1.id)
jogador10 = Jogador(10, "João", "jp", datetime.date(1999, 7, 9), 13, "atacante", 1, 2, "SUSPENSO", time1.id)
jogador11 = Jogador(11, "Pietro", "Pepeu", datetime.date(1999, 7, 9), 45, "meio", 1, 0, "TÁ PRA JOGO", time1.id)
jogador12 = Jogador(12, "Marcos", "Leu", datetime.date(1999, 7, 9), 9, "zagueiro", 1, 1, "TÁ PRA JOGO", time1.id)
jogador13 = Jogador(13, "Guilherme", "Gui", datetime.date(1999, 7, 9), 5, "meio", 1, 0, "TÁ PRA JOGO", time1.id)
jogador14 = Jogador(14, "Juliano", "Jr", datetime.date(1999, 7, 9), 0, "atacante", 1, 0, "TÁ PRA JOGO", time1.id)

#Salvando os jogadores no banco de dados
jogador0.save()
jogador2.save()
jogador5.save()
jogador6.save()
jogador7.save()
jogador8.save()
jogador10.save()
jogador11.save()
jogador12.save()
jogador13.save()
jogador14.save()


#Printar minha lista de jogadores e o time que eles pertencem
print(time1)

a = [jogador0, jogador2, jogador5, jogador6, jogador7, jogador8, jogador10, jogador11, jogador12, jogador13, jogador14]
for g in a:
 	print(g)

#Criação do segundo time

time2 = Time(2, 'Inter','colorado', datetime.date(1909, 4, 4))
time2.save()

#Criando os jogadores do segundo time com seus devidos dados

jogador3 = Jogador(3, "Matias", "ti", datetime.date(1999, 7, 9), 6, "goleiro", 1, 2, "SUSPENSO", time2.id)
jogador4 = Jogador(4, "Cassio", "K", datetime.date(1999, 7, 9), 9, "zagueiro", 1, 2, "SUSPENSO", time2.id)
jogador9 = Jogador(9, "luca", "te", datetime.date(1999, 7, 9), 12, "zagueiro", 1, 2, "SUSPENSO", time2.id)
jogador15 = Jogador(15, "Diego 2", "Dih", datetime.date(1999, 7, 9), 3, "zagueiro", 1, 0, "TA PRA JOGO", time2.id)
jogador16 = Jogador(16, "Gabriel", "Gabi", datetime.date(1999, 7, 9), 67, "meio", 1, 2, "SUSPENSO", time2.id)
jogador17 = Jogador(17, "Ismael", "--", datetime.date(1999, 7, 9), 58, "meio", 1, 2, "SUSPENSO", time2.id)
jogador18 = Jogador(18, "Anderson", "--", datetime.date(1999, 7, 9), 89, "goleiro", 1, 2, "SUSPENSO", time2.id)
jogador19 = Jogador(19, "Eduardo 2", "Edu", datetime.date(1999, 7, 9), 50, "meio", 1, 2, "SUSPENSO", time2.id)
jogador20 = Jogador(20, "Alex", "--", datetime.date(1999, 7, 9), 53, "zagueiro", 1, 2, "SUSPENSO", time2.id)
jogador21 = Jogador(9, "José", "zé", datetime.date(1999, 7, 9), 57, "atacante", 1, 0, "TA PRA JOGO", time2.id)
jogador22 = Jogador(10, "Agnaldo", "guino", datetime.date(1996, 9, 4), 45, "meio", 1, 4, "SUSPENSO", time2.id)

#Salvando os jogadores no banco de dados
jogador3.save()
jogador4.save()
jogador9.save()
jogador15.save()
jogador16.save()
jogador17.save()
jogador18.save()
jogador19.save()
jogador20.save()
jogador21.save()
jogador22.save()

#Printar minha lista de jogadores e o time que eles pertencem
print(time2)
v = [jogador3, jogador4, jogador9, jogador15, jogador16, jogador17, jogador18, jogador19, jogador20, jogador21, jogador22]
for x in v:
 	print(x)







# time1.relacionar_jogadores([
# jogador0,
# jogador2,
# jogador3,
# jogador4,
# jogador5,
# jogador6,
# jogador7,
# ogador8,
# jogador9,
# jogador10,
# jogador11,
# jogador12,
# jogador13,
# jogador14,
# jogador15,
# jogador16,
# jogador17,
# jogador18,
# jogador19,
# jogador29,])

# print(time1)