# hora das listas
lista = [2, 5, 3, 6, 1, 9, 4]
print(lista)
#a lista é mutável
lista[2] = 10
print(lista)
#a lista pode ser adicionado valores
lista.append(7)
print(lista)
#a lista pode ser listada em ordem
lista.sort()
print(lista)
#também é possivel inverter a ordem para descrescente
lista.sort(reverse=True)
print(lista)
#para realizar a contagem de itens na lista
print(f'A lista tem {len(lista)} itens registrados')
#é possivel inserir um valor
lista.insert(2, 0)
print(lista)
#é possivel remover um item atraves do comando pop e existe o comando remove
lista.pop()
print(lista)
#pode-se remover algo específico
lista.pop(2)
print(lista)
#lista organizada
for c, l in enumerate(lista):
    print(f'Na posição {c} encontrei o item {l}')
#criar uma cópia de uma lista
b = lista[:]
b[2] = 11
print(f'Lista A: {lista}')
print(f'Lista B: {b}')
#a lista pode ser clonada e vinculada entre si
#cuidado com isso, se uma lista for vinculada em uma nova
#e a nova for alterada, a original também é alterada
#cuidado ao usar = ao tentar copiar