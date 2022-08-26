#faça um programa que leia
#5 VALORES NUMERICOS e guarde-os
#em uma LISTA

#No final, mostre qual foi o MAIOR
#e MENOR valor digitado e as suas
#respectivas POSIÇOES na lista
mas = 0
mini = 0
lista = []
for l in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
for m, l in enumerate(lista):
    if l == max(lista):
        mas = m+1
    elif l == min(lista):
        mini = m+1
print(f'O valor maior digitado foi: {max(lista)} na {mas}ª posição')
print(f'O valor menor digitado foi: {min(lista)} na {mini}ª posição')