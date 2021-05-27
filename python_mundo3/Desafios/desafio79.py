#crie um programa onde o usuário possa
#digitar VARIOS VALORES NUMERICOS e
#cadastre-os em uma LISTA. Caso o número
#já exista lá dentro, ele NAO SERA ADICIONADO,
#no final, serao exibidos todos os VALORES
#UNICOS digitados, em ORDEM CRESCENTE
lista = []
valor = 0
ex = 0
cont = ''
lista.append(int(input('Digite um valor: ')))
cont = str(input('Deseja continuar? S/N\nR: ')).upper()
if cont == 'S':
    while True:
        valor = int(input('Digite outro valor: '))
        for l, v in enumerate(lista):
            if valor == v:
                print('valor já existente')
                ex = 1
            if ex == 1:
                break
            else:
                ex = 0
        if ex == 0:
            lista.append(valor)
        cont = str(input('Deseja continuar? S/N\nR: ')).upper()
        if cont == 'S':
            continue
        elif cont == 'N':
            break
print('Segue numero digitados em ordem crescente:')
lista.sort()
for l, v in enumerate(lista):
    print(f'Valor: {v}| Na posição: {l+1}')