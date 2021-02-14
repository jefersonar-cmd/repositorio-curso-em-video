#faca um programa que calcule
# a soma entre todos os numeros impares que sao multiplos de 3
# e que se encontram no intervalo de 1 ate 500
soma = 0
print('numeros primos divisiveis por 3')
for c in range(1, 500+1):
    if c % 3 == 0:
        soma += c
print('A soma de todos os impares sao: {}'.format(soma))
print('fim teste')