#desenvolva um programa que
#leia 6 numeros inteiros e mostra a soma
#daqueles que forem PARES
#se for IMPAR desconsiderar
print('soma de numeros')
soma = 0
pares = []
for c in range(1, 6+1):
    user = int(input('Infome um numero aleatorio: '))
    if user % 2 == 0:
        soma += user
        pares.append(user)
print('A soma dos valores pares informados é de {}'.format(soma))
print('Os numeros pares foram {}'.format(pares))