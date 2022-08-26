# crie um programa que tenha a FUNCAO LEIAINT(), que vai funcionar de forma semelhante à função INPUT do PYTHON, só que fazendo VALIDACAO para aceitar apenas um valor numérico.
# EX.: n = leiaINT('Digite um n: ')
def leiaINT(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mDigite um número inteiro válido!\33[m')
        if ok:
            break
    return valor


val = leiaINT('Digite algo: ')
print(f'Você digitou o valor: {val}')
