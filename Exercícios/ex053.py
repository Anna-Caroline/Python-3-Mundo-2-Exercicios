'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) #elimina os espaços internos
inverso = junto[::-1] #forma mais simples, usando fatiamento de string
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}.'.format(junto, inverso), end = ' ')
if junto == inverso:
    print('Portanto, TEMOS UM PALÍNDROMO.')
else:
    print('Portanto, NÃO TEMOS UM PALÍNDROMO.')

