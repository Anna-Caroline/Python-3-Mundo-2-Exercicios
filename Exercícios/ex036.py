valor = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você deseja pagar? '))
prestacao = (valor)/(anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valor, anos), end = ' ')
print('a prestação será de {:.2f}!'.format(prestacao))
if prestacao <= salario * 0.3:
    print('\033[1;32;40m Empréstimo APROVADO! \033[m')
else:
    print('\033[1;31;40m Empréstimo NEGADO! \033[m')

