# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
listaBase = []
listaPar = []
listaImpar = []
cont = 'S'
while cont == 'S':
    n = int(input('Digite um valor: '))
    listaBase.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    cont = str(input('Deseja continuar?\n[S/N]'))
    cont = cont.upper()
    if cont == 'S':
        continue
    else:
        break
print(f'A lista criada tem {len(listaBase)} itens com os valores {listaBase}\nSeparando os valores em pares {listaPar}\nE em impares {listaImpar}')