nome =  str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem! {}'.format(nome.replace('Gustavo', 'Joaquim')))
else:
    print('Bom dia, {}'.format(nome))