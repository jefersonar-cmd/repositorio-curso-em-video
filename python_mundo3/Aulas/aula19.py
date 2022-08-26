# Variaveis compostas:
# Tuplas, Listas e Dicionario

pessoas = {'nome': 'Jefferson', 'sexo': 'M', 'idade': 22}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(f"Values: {pessoas.values()}")
print(f"Keys: {pessoas.keys()}")
print(f"Items: {pessoas.items()}")
print('Acessando Dicionário por chave, usando FOR')
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('deletando item')
del pessoas['sexo']
print(pessoas)
print('-='*30)
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v, in e.items():
        print(f'O campo {k} tem valor {v}.')

