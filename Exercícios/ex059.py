# Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('Opção [1] = somar\n'
          '    Opção [2] = multiplicar\n'
          '    Opção [3] = maior\n'
          '    Opção [4] = novos números\n'
          '    Opção [5] = sair do programa')
    opção = int(input('Digite qual a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Informe o primeiro valor.'))
        n2 = int(input('Informe o segundo valor.'))
    elif opção == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida. Digite novamente.')
    print('-=' * 16)
print('Fim do programa, volte sempre.')
