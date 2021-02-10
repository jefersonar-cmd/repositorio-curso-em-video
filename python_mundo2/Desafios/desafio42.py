#refaça o desafio 35 do triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
#equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes
print('-='*20)
print('Analisador de Segmentos')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 + r2 < r3 and r1 + r3 < r2 and r2 + r3 < r1:
    print('Não é um triangulo')
elif r1 == r2 and r1 == r3:
    print('Equilátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Isósceles')
else:
    print('Escaleno')