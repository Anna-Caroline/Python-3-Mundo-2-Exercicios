peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
#elif imc >= 18.5 and imc < 25:
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso normal.')
elif 25<= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida!')