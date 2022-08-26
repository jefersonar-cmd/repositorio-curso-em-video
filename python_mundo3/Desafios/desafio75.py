#Desenvolva um programa que leia QUATRO VALORES e guarde-os
#em uma TUPLA. No final, mostre:
#A) Quantas vezes apareceu o valor 9
#B) Em que posição foi digitado o primeiro valor 3
#C) Quais foram os numeros PARES
print('Registrando valores na Tupla')
tuplapri = ()
tuplapar = ()
nove = 0
tres = 0
for c in range(0, 4):
    valor = int(input('Informe um valor'))
    tuplapri += (valor,)
    if valor % 2 == 0:
        tuplapar += (valor,)
print('A) Quantas vezes aparecem o número 9:')
for n in range(0, len(tuplapri)):
    if tuplapri[n] == 9:
        nove += 1
if nove > 0:
    print(f'O número 9 aparece por {nove}x')
else:
    print('O valor 9 não aparece em nenhum momento')
print('B) Em que posição foi digitado o primeiro valor 3')
for t in range(0, len(tuplapri)):
    if tuplapri[t] == 3:
        tres = t+1
        break
if tres > 0:
    print(f'Aparece na {tres}ª posição')
else:
    print('O número 3 não aparece em nenhum das posições')
print('C) Quais foram os valores pares')
for p in range(0, len(tuplapar)):
    print(f'{tuplapar[p]}')