#faca um programa que
#leia o SEXO de uma pessoa, mas aceite
#os valores M ou F
#caso esteja errado, peca a digitacao novamente
#ate ter um valor correto
print('Adicionando Info')
sex = 'Z'
while sex != 'M' and sex != 'F':
    sex = str(input('Qual seu SEXO? [M (masculino)/F (feminino)]\n')).upper()
print('Obrigado pela Informacao')