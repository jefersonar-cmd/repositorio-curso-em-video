# variáveis e compostas (Listas)

print('Lista Simples e Compostas')
teste = list()
teste.append('Ravezeiro')
teste.append(22)
print(f'Lista simples:\n{teste}')
galera = []
galera.append(teste[:])
print(f'Lista dentro de lista:\n{galera}')
teste[0] = 'Argente'
teste[1] = 22
galera.append(teste[:])
print(f'Listas dentro de lista:\n{galera}')

print('Outro exemplo de lista')
galera2 = [
    ['Argente123'],
    ['Ravezeiro_85'],
    ['ProgramadorAos30'],
    ['VictorGalvao']
]
for i in galera2:
    print(f'Declarando minha galera: {i[0]}')

print('Adicionando conteudo a lista')
lista = []
while True:
    nome = input(str('Digite um nick: '))
    continuar = input(str(f'Deseja adicionar mais nicks a lista? [s/n]\n'))
    lista.append(nome)
    if continuar.upper() == 'S':
        continue
    else:
        break

print('Segue o nome da galera da Twitch maravilinda!')
for n in lista:
    print(f'Nick: {n[0]}')
# modificando exemplo do Gustavo Guaraná
newLista = []
temp = []
demaior = demenor = 0
for c in range(0,5):
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite a idade: ')))
    newLista.append(temp[:])
    temp.clear()

for l in newLista:
    if l[1] >= 18:
        print(f'{l[0]} pode ser preso.')
        demaior += 1
    else:
        print(f'{l[0]} não pode ser preso.')
        demenor += 1

print(f'Temos {demaior} que podem ser presos e {demenor} que infelizmente não podem ser presos.')