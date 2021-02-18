#crie um programa que
#leia VARIOS NUMEROS INTEIROS pelo teclado.
#O programa so vai para quando o usuario digitar
#o valor 999, que e a CONDICAO DE PARADA.
#No final, mostre QUANTOS NUMEROS foram digitados e qual a SOMA entre eles
#(DESCONSIDERANDO O 999)
print("Programa de SLA")
cont = 0
soma = 0
while True:
    user = int(input('Informe um numero (Digite 999 para parar): '))
    if user == 999:
        break
    soma += user
    cont += 1
print(f'Foram digitados {cont} e a soma de todos eles {soma}')
print('Fim PROGRAMA SLA')