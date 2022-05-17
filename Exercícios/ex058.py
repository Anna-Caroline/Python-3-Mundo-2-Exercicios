'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
computador = randint(0,10)
print('-='*20)
print('Vou pensar em um número inteiro entre 0 e 10, tente adivinhar qual foi!')
print('-='*20)
jogador = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(3)
palpite = 0
while computador != jogador:
    jogador = int(input('Você errou, eu pensei em {} e você disse {}. \nTente mais uma vez:'.format(computador, jogador)))
    computador = randint(0, 10)
    palpite += 1
print('Parabéns, você acertou com {} tentativas! Eu pensei mesmo no número {}.'.format(palpite,computador))

'''from random import randint
computador = randint(0,10)
print ('Sou seu computador. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar?')
acertou = False
while not acertou: 
    jogador = int(input('Qual é o seu palpite?'))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez.')
        elif jogador > computador:
            print('Menos... Tente outra vez.')
print('Acertou!')'''