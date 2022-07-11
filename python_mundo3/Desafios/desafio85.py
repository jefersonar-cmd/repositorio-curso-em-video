# Crie um programa onde o usuário possa digitar SETE VALORES NUMERICOS e cadastre-os em uma LISTA UNICA que matenha separados os valores PARES e IMPARES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.
# Obs.: Usar uma unica lista composta
num = [
    [],
    []
]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')
print('-=' * 30)
print('Fim do programa! Volte sempre!')