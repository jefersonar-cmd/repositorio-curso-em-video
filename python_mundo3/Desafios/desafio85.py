# Crie um programa onde o usuário possa digitar SETE VALORES NUMERICOS e cadastre-os em uma LISTA UNICA que matenha separados os valores PARES e IMPARES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.
# Obs.: Usar uma unica lista composta
listaGlobal = [
    [],
    []
]
for n in range(0, 7):
    numero = int(input('Digite um número: '))
    if n == 0 or len(listaGlobal[0]) == 0 or len(listaGlobal[1]) == 0:
        if numero % 2 == 0:
            listaGlobal[0].append(numero)
            print(f'Positivo: {len(listaGlobal[0])}')
        else:
            listaGlobal[1].append(numero)
            print(f'Negativo: {len(listaGlobal[1])}')
    else:
        if numero % 2 == 0:
            pos = 0
            while pos < len(listaGlobal[0]):
                if numero <= listaGlobal[0][pos]:
                    if numero == listaGlobal[0][pos]:
                        print('Numero repetido')
                    else:
                        listaGlobal[0].insert(pos, numero)
                        print(f'Positivo: {len(listaGlobal[0])}')
                        break
                else:
                    pos += 1
        else:
            pos = 0
            while pos < len(listaGlobal[1]):
                if numero <= listaGlobal[1][pos]:
                    if numero == listaGlobal[1][pos]:
                        print('Numero repetido')
                    else:
                        listaGlobal[1].insert(pos, numero)
                        print(f'Negativo: {len(listaGlobal[1])}')
                        break
                else:
                    pos += 1

print(f'Lista de pares e impares:\nPares: {listaGlobal[0]}\nImpares: {listaGlobal[1]}')