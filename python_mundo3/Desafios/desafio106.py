# faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do PYTHON. o usuário vai digitar o COMANDO e o MANUAL vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se ENCERRARA.
# OBS.: use CORES
def manual(comando):
    while True:
        print('='*20)
        c = str(input(comando))
        print('='*20)
        if c.upper() == "FIM":
            print('\033[0;30;43m='*20)
            print('FIM')
            print('='*20, '\033[m')
            break
        elif c.strip() == '' or c.isnumeric():
            print('\033[0;30;41m='*20)
            print('Comando não encontrado!')
            print('='*20, '\033[0;0m')
        else:
            print('\033[0;30;42m='*20)
            print(help(c))
            print('='*20, '\033[m')


manual('Digite um comando: ')