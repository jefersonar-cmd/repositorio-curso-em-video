#faca um programa que
#leia um Numero Inteiro e diga se ele
#É ou Nao um Numero PRIMO
print('Numeros primos')
primo = int(input('Informe um numero: '))
contador = 0
print('Ele é divisivel por:')
for c in range(1, primo+1):
    if primo % c == 0:
        contador += 1
        print(c, end=' ')
if contador == 2:
    print('\nO numero {} informado é um numero primo'.format(primo))
else:
    print('\nO numero {} não é um numero primo'.format(primo))