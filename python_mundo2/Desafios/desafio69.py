#crie um programa que
#leia a IDADE e o SEXO de VARIAS PESSOAS
#a cada pessoa cadastrada, o programa devera
#perguntar se o USUARIO quer ou nao continuar
#no final mostre
#A)Quantas pessoas tem mais de 18 ANOS
#B)Quantos HOMENS foram cadastrados
#C)Quantas MULHERES tem menos de 20 ANOS
femMen = 0
maisDezoito = 0
prossiga = 'S'
homemIdade = []
mulherIdade = []
while True:
    sexo = str(input('Informe o Sexo [M/F]: ')).upper()
    if sexo == 'M':
        idade = int(input('Informe a idade: '))
        if idade >= 18:
            maisDezoito += 1
            homemIdade.append(idade)
            prossiga = str(input('Deseja prosseguir?\n[S/N] ')).upper()
            if prossiga == 'S':
                continue
            else:
                break
        else:
            homemIdade.append(idade)
            prossiga = str(input('Deseja prosseguir?\n[S/N] ')).upper()
            if prossiga == 'S':
                continue
            else:
                break
    elif sexo == 'F':
        idade = int(input('Informe a idade: '))
        if idade <= 20:
            if idade >= 18:
                maisDezoito += 1
                femMen += 1
                mulherIdade.append(idade)
                prossiga = str(input('Deseja prosseguir?\n[S/N] ')).upper()
                if prossiga == 'S':
                    continue
                else:
                    break
            else:
                femMen += 1
                mulherIdade.append(idade)
                prossiga = str(input('Deseja prosseguir?\n[S/N] ')).upper()
                if prossiga == 'S':
                    continue
                else:
                    break
        else:
            mulherIdade.append(idade)
            prossiga = str(input('Deseja prosseguir?\n[S/N] ')).upper()
            if prossiga == 'S':
                continue
            else:
                break
    else:
        print('Opcao invalida, tente novamente')
        continue
print(f'{maisDezoito} Pessoas tem mais de 18 anos')
print(f'{len(homemIdade)} Homens foram cadastrados')
print(f'{femMen} Mulheres tem menos de 20 anos')
print(f'{len(homemIdade)+len(mulherIdade)}')