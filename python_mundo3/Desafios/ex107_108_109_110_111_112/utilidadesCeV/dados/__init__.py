def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            if n.index(','):
                n.replace(',', '.')
        else:
            print(f'\33[0;31mERRO: {n} não é um dado válido!\33[m')
        if ok:
            break
    return valor