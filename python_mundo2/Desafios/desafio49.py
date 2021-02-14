#refaca o DESAFIO 9
#mostrando a tabuada de um numero que o usuario escolher
#so que agora utilizando um laco FOR
print('tabuada')
user = int(input('Infome um numero: '))
for c in range(0, 10+1):
    print('{} X {}= {}'.format(c, user, user * c))
print('FIM')