# sequencia de fibonacci

limite = int(input('escreva o limite para o contador: '))
n1 = 0
n2 = 1
print(n1, '\n')
print(n2, '\n')

while limite > 0:
    n1 = n1 + n2
    print(n1, '\n')
    n2 = n1 + n2
    print(n2, '\n')
    limite -= 1
