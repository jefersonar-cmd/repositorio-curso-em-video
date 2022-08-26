# Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre um BOLETIM contendo a MEDIA de cada um e permita que o usuario possa mostrar as NOTAS de cada aluno idividualmente.

alunoNotas = []
listaAlunos = []

while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunoNotas.append(nome)
    alunoNotas.append(nota1)
    alunoNotas.append(nota2)
    alunoNotas.append(media)
    listaAlunos.append(alunoNotas[:])
    alunoNotas.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"Nome":<4}{"N1":>8}{"N2":>8}{"Média":>8}')
print('-' * 30)
for i in listaAlunos:
    print(f'{i[0]:<4}{i[1]:>8.1f}{i[2]:>8.1f}{i[3]:>8.1f}')
print('-' * 30)
while True:
    nome = str(input('Nome do Aluno: '))
    for i in listaAlunos:
        if nome == i[0]:
            print(f'Notas do Aluno {nome}: {i[1]} e {i[2]}')
            print(f'Média do Aluno {nome}: {i[3]}')
            break
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-=' * 30)
print('Fim do Programa')