#refaca o DESAFIO 51, lendo
#o PRIMEIRO TERMO e a RAZAO de uma PA
#mostrando os 10 PRIMEIRO TERMOS da progressao
#usando a estrutura WHILE
print('Progressao aritmetica')
print('10 termos')
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
cont = 10
while cont != 0:
    print(termo, end=' ')
    termo += razao
    cont -= 1
print('Fim')