#crie um programa que
#simule um CAIXA ELETRONICO
#no inicio, pergunte ao usuario qual sera
#o VALOR A SER SACADO (NUMEROS INTEIROS) e o programa
#deve informar quantas CEDULAS de cada valor serao entregues
#OBS.: Considere que o caixa possui cedulas de 50, 20, 10 e 1
print('-='*20)
print('Caixa Eletronico')
print('=-'*20)
sacar = int(input('Qual valor a ser sacado?\nR$'))
cont = 0
total = 0
resto = 0
while True:
    cont += 1
    if sacar < 50:
        resto = sacar
        break
    else:
        cont += 1
        total += 50
        sacar -= 50
        continue
print(f'Vai ser retirado {cont} notas de 50, totalizando {total}, restando apenas {resto}')