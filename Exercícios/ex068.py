''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('Vamos jogar Par ou Ímpar!')
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}.', end = ' ')
    print('Deu par!'if total % 2 == 0 else 'Deu impar!')
    if tipo =='P':
        if total %2 == 0:
            print('Você venceu!', end = ' ')
            v += 1
        else:
            print('Você perdeu!', end = ' ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!', end = ' ')
            v += 1
        else:
            print('Você perdeu!', end = ' ')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes.')
