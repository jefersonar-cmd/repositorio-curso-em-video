#desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 ate 30: sobrepeso
#30 ate 40: obesidade
#acima de 40: obesidade morbida
print('-='*20)
print('Calculo IMC')
print('=-'*20)
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu Peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso, seu imc é {}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal, seu imc é {}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso, seu imc é {}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade, seu imc é {}'.format(imc))
elif imc >= 40:
    print('Obesidade Morbida, seu imc é {}'.format(imc))
