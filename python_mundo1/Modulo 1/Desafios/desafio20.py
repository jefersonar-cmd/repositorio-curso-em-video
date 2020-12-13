# o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada

from random import shuffle
num = 1
cont = 0
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem de alunos a apresentar')

while cont < 4:
    print('{}º Aluno: {}'.format(num, list[cont]))
    cont += 1
    num += 1