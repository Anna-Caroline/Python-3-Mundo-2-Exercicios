#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
#f = factorial(n)
#print('O fatorial de {} é {}'.format(n, f))
c = n
f = 1
print('Calculando {}! = '.format(n), end= '')
while c > 0:
    print(c, end = '')
    print(' x ' if c >1 else ' = ', end = '')
    f = f * c
    c -= 1
print('{}.'.format(f))

''' usando o for: n = int(input('digite um numero'))
f = 1
for n in range (n, 1, -1):
    f = f * n
print (f)'''
