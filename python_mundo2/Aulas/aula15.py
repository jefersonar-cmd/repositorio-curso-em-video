cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
    if cont < 10+1:
        continue
    else:
        break
print('Acabou')