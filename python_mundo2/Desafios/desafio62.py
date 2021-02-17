#melhore o DESAFIO 61,
#perguntando se o usuario quer mostrar
#mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 TERMOS
print('Progressao aritmetica')
print('10 termos')
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
cont = 10
while termo != 0:
    while cont != 0:
        print(termo, end=' ')
        termo += razao
        cont -= 1
    escolha = int(input('\nGostaria de pedir mais termos?\n1- sim\n0- nao\nEscolha: '))
    if escolha == 1:
        termo = int(input('Informe o termo: '))
        razao = int(input('Informe a razao: '))
        cont = 10
    else:
        termo = escolha
print('Fim')