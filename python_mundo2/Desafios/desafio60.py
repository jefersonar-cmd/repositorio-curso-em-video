#faca um programa que
#leia um NUMERO qualquer e mostre o seu FATORIAL
#EX: 5 = 5x4x3x2x1 = 120
print('FATORANDO o FATOR')
user = cont = int(input('Informe um numero: '))
valor = ''
total = user
while cont != 1:
    cont -= 1
    valor += str(cont+1) + ' X '
    total = total * cont
repli = len(valor) - 2
print('{} = {} x 1 = {}'.format(user, valor[0:repli], total))