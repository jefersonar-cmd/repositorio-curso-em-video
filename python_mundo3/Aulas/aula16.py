#tupla padrão
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

#fatiamento
print(lanche[-3:])

#Tuplas são imutáveis
#Aparecer textos sem parentes e haspas simples
#Modo Simples:
for comida in lanche:
    print(f'Eu vou comer {comida}')
#Modo in Range:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#Modo in Enumerate:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#Organizar conteudo da Tupla em Ordem
print(sorted(lanche))

#concatenação com Tupla
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
#contar quantos numeros 5 (por exemplo) na tupla
print(c.count(5))
#mostra em que posição está um número na Tupla
print(c.index(8))
#Tupla com dados entre caractere e numeros
pessoa = ('Jefferson', 21, 'M', 69.9)
del(pessoa)
print(pessoa)