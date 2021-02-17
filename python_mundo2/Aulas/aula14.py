for c in range(1, 10):
    print(c, end=' ')
print('Fim FOR Repetico')
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('Fim While Repeticao')
for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim For Leitor')
c = 1
while c != 0:
    c = int(input('Digite um valor: '))
print('Fim While Leitor')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim While Escolha')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Fim While Par Impar')