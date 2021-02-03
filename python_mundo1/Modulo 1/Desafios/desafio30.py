#crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
print('{:=^30}'.format('Verificador PAR ou IMPAR'))
n1 = int(input('Informe um número: '))
resultado = n1 % 2
if resultado == 0:
    print('Par')
else:
    print('Impar')
