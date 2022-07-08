# Aprimore o DESAFIO 86, mostrando no final:
#a) A SOMA de todos os VALORES PARES digitados
#b) A SOMA dos valores da TERCEIRA COLUNA
#c) O MAIOR valor da SEGUNDA COLUNA

print('Matriz')
matriz = [
    [],
    [],
    []
]

linha = 0
qtd = 0
while True:
    numero = int(input('Digite um número: '))
    matriz[linha].append(numero)
    if len(matriz[linha]) == 3:
        linha += 1
        if linha == 3:
            break

print('Matriz 3x3')
for l in range(0, 3):
    print(matriz[l])

print('\nA)')
pares = 0
for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])):
        if matriz[l][c] % 2 == 0:
            pares += 1

print(f'Pares total: {pares}')
print('\nB)')
terceira = 0
for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])):
        if c == 2:
            terceira += matriz[l][c]

print(f'Soma da Terceira coluna: {terceira}')
print('\nC)')
lista = []
for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])-1):
        if c == 1:
            lista.append(matriz[l][c])

print(f'O maior numero da segunda coluna: {max(lista)}')