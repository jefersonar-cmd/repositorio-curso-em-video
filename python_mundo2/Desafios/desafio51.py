#desenvolva um programa que
#leia o Primeiro Termo e a Razao de uma PA
#No final, mostre os 10 primeiros termos dessa progressao
print('Progressao aritmetica')
print('10 termos')
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
for c in range(1, 10+1):
    print(termo, end=' ')
    termo += razao
print('Fim')