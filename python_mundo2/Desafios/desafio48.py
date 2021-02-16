#faca um programa que calcule
# a soma entre todos os numeros impares que sao multiplos de 3
# e que se encontram no intervalo de 1 ate 500
soma = 0
impares = 0
print('numeros impares divisiveis por 3')
for c in range(1, 500+1):
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
            impares += 1
print('A soma de todos os {} impares sao: {}'.format(impares, soma))
print('fim teste')