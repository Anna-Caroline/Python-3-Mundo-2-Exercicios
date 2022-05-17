'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
totalgasto = 0
maisdemil = 0
menor = 0
cont = 0
barato = ' '
while True:
    nomeprod = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Qual o preço do produto? R$ '))
    cont += 1
    totalgasto += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nomeprod
    #else:
        #if preço < menor:
            #menor = preço #comandos iquais aos de cima, então pode  juntar com o or preço < maior
            #barato = nomeprod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {totalgasto:.2f}')
print(f'Ao todo foram {maisdemil} que custaram mais de mil reais.')
print(f'O produto mais barato foi {barato} que custou R$ {menor:.2f}')
