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
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 30)

print('Matriz 3x3')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print('\nA)')
pares = 0
for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

print(f'Pares total: {pares}')
print('-=' * 30)
print('\nB)')
terceiraColuna = 0
for l in range(0, len(matriz)):
    terceiraColuna += matriz[l][2]
print(f'Soma da terceira coluna: {terceiraColuna}')
print('-=' * 30)
print('\nC)')
segundaColuna = []
for l in range(0, len(matriz)):
    segundaColuna.append(matriz[l][1])
print(f'O maior numero da segunda coluna: {max(segundaColuna)}')