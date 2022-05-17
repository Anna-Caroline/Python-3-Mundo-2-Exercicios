#Alistamento
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos no ano de {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será no ano de {}'.format(atual + (18-idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))