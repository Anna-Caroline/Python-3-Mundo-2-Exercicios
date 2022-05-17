# Gerenciador de pagamentos
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] duas vezes cartão
[4] três vezes ou mais cartão''')
opcao = int(input('Digite a forma de pagamento: '))
if opcao == 1:
    total = preço - (preço * 0.1)
    print('')
elif opcao == 2:
    total = preço - (preço * 0.05)
elif opcao == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 0.2)
    totalparc = int(input('Em quantas parcelas você deseja pagar? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}, COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('\033[1;31;40m OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')
print('Sua compra de R$ {:.2f}, vai custar R$ {:.2f} no final.'.format(preço, total))
