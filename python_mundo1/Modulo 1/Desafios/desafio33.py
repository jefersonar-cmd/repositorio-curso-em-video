#faca um programa que leia tres numeros e mostre qual é o MAIOR e qual é o MENOR
print('{:=^50}'.format('Descobrindo o MAIOR e o MENOR'))
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2:
    print('O Maior é: {}'.format(n1))
    if n2 > n3:
        print('O menor é: {}'.format(n3))
    else:
        print('O menor é: {}'.format(n2))
elif n2 > n3:
    print('O maior é: {}'.format(n2))
    if n1 > n3:
        print('O menor é: {}'.format(n3))
    else:
        print('O menor é: {}'.format(n1))
else:
    print('O maior é: {}'.format(n3))
    if n1 > n2:
        print('O menor é: {}'.format(n2))
    else:
        print('O menor é: {}'.format(n1))