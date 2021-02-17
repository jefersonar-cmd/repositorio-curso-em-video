#crie um programa que leia
#DOIS VALORE e mostre um MENU na tela:
#[1]somar[2]multiplicar[3]maior
#[4]novos numeros[5]sair do programa
#seu programa deverá realizar a operacao solicidada em cada caso
print('Programa Sla')
n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))
escolha = 0
while escolha != 5:
    print('''
    O que deseja fazer?
    [1] Somar
    [2] Multiplicar
    [3] Verificar Maior
    [4] Informar novos valores
    [5] Sair do Programa
    ''')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif escolha == 2:
        multi = n1 * n2
        print('A multiplicacao de {} x {} = {}'.format(n1, n2, multi))
    elif escolha == 3:
        if n1 > n2:
            print('O primeiro numero eh maior')
        else:
            print('O segundo numero eh maior')
    elif escolha == 4:
        n1 = int(input('Informe um novo numero: '))
        n2 = int(input('Novamente: '))
    else:
        print('''
        Deseja sair mesmo?
        [5] SIM
        [6] NAO
        ''')
        escolha = int(input('Escolha: '))
        if escolha == 5:
            continue
        else:
            continue
print('Obrigado por Utilizar')