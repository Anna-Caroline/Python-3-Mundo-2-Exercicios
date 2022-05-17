'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
n = c = soma = 0 #pode atribuir todas as variáveis em uma única linha
n = int(input('Digite o número [999 para parar.]:'))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite o número [999 para parar.]:'))
print('Você digitou {} números'.format(c))
print('E a soma entre eles foi {}'.format(soma))
print('Acabou.')