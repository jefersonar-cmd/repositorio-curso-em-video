#faca um programa que
#mostre a TABUADA de VARIOS NUMEROS
#um de cada vez, para cada valor digitado pelo usuario
#O programa sera INTERROMPIDO qunado o numero solicitado for NEGATIVO
print('Tabuada')
cont = 0
while True:
    user = int(input('Informe um numero a ser multiplicado: '))
    if user >= 0:
        while cont < 11:
            print(f'{user} X {cont} = {user*cont}')
            cont += 1
        cont = 0
    else:
        break
print('Fim Programa')