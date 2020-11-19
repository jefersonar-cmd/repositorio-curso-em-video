# faça uma aplicação que
# leia um numero inteiro qualquer e
# mostre na tela a sua tabuada

print('{:=^30}'.format('Tabuada'))
n1 = int(input('Informe um número \na ser feito a tabuada: '))
cont = 0
print('{:^30}'.format('Resultado'))
while cont < 11:
    print('{} x {} = {}'.format(n1, cont, n1*cont))
    cont+=1