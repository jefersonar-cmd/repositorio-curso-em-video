#faca um programa que
#leia o PESO de CINCO PESSOAS
#no final, mostre qual foi o MAIOR e o MENOR peso lidos
print('Verificador de peso')
peso = []
maior = 0
menor = 0
for c in range(1, 6):
    user = float(input('Informe o peso da {}ª Pessoa: '.format(c)))
    peso.append(user)
maior = max(peso, key=int)
menor = min(peso, key=int)
print('maior peso {}'.format(maior))
print('menor peso {}'.format(menor))