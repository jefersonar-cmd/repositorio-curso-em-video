#Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a Base de Converção:
#1 para Binario
#2 para Octal
#3 para Hexadecimal
print('-='*20)
print('Conversor')
print('=-'*20)
user = int(input('informe um numero qualquer: '))
opcao = int(input('Para qual base deseja converter?\n1- Binário\n2- Octal\n3- Hexadecimal\nEscolha: '))
if opcao == 1:
    print('{0:08b}'.format(user))
elif opcao == 2:
    print(oct(user))
elif opcao == 3:
    print(hex(user))