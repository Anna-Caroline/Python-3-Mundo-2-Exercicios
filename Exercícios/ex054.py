'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao total, temos {} pessoas maior de idade;'.format(totmaior), end = ' ')
print('e {} pessoas menor de idade.'.format(totmenor))
