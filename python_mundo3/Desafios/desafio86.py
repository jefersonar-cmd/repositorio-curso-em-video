# Crie um programa que crie uma MATRIZ de DIMENSAO 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a MATRIZ na tela, com a formatação correta.
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