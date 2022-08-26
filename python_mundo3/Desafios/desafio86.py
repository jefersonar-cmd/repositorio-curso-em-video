# Crie um programa que crie uma MATRIZ de DIMENSAO 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a MATRIZ na tela, com a formatação correta.
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
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print('Fim do programa! Volte sempre!')