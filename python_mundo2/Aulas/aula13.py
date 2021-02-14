for c in range(0, 6):
    print('OI')
print('FIM')
#
for c in range(6, 0, -1):
    print('OI')
print('FIM')
#
for c in range(0, 7, 2):
    print('OI')
print('FIM')
#
n = int(input('Informe um numero'))
for c in range(0, n+1):
    print(c)
print('FIM')
#
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor'))
    s += n
print('somatorio de todos sao {}'.format(s))