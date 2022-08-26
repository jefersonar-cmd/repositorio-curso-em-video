# Modularização
# Surgiu no inicio da década de 60
# Sistema ficando cada vez maiores
# Foco: dividir um programa grande
# Foco: aumentar a legibilidade
# Foco: facilitar a manutenção
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

# Vantagens
# Organização do código
# Facilidade na manutenção
# Reutilizar em outros projetos

# Pacotes