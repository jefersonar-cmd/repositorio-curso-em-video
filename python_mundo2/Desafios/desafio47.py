#crie um programa que mostre na tela
#todos os número pares que estao no intervalo entre 1 a 50
print('numeros pares de 1 a 50')
for c in range(1, 50+1):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')