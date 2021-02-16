#desenvolva um programa que
#leia o NOME, IDADE e SEXO de 4 PESSOAS
#No final mostre:
#A MEDIA DE IDADE do grupo
#qual e o nome do HOMEM MAIS VELHO
#quantas mulheres tem MENOS DE 20 anos
print('Media de Idade do Grupo')
nomeMas = []
sexMas = []
idadMas = []
nomeFem = []
sexFem = []
idadFem = []
idade = 0
media = 0
for c in range(1, 5):
    sex = int(input('Qual sexo?\n0- mulher\n1- homem\nR:'))
    if sex == 0:
        sexFem.append('Feminino')
        nomeFem.append(str(input('Informe o nome: ')))
        idade = int(input('Informe a idade: '))
        idadFem.append(idade)
        media += idade
        continue
    elif sex == 1:
        sexMas.append('Masculino')
        nomeMas.append(str(input('Informe o nome: ')))
        idade = int(input('Informe a idade: '))
        idadMas.append(idade)
        media += idade
        continue
media = media / 4
print('A idade Média do grupo é: {}'.format(media))
if idadMas[0] > idadMas[1]:
    print('O homem mais velho se chama {} e tem {} anos'.format(nomeMas[0], idadMas[0]))
else:
    print('O homem mais velho se chama {} e tem {} anos'.format(nomeMas[1], idadMas[1]))
if idadFem[0] <= 20:
    print('A mulher que tem menos que 20 anos se chama {} e tem {} anos'.format(nomeFem[0], idadFem[0]))
elif idadFem[1] <= 20:
    print('A mulher que tem menos que 20 anos se chama {} e tem {} anos'.format(nomeFem[1], idadFem[2]))