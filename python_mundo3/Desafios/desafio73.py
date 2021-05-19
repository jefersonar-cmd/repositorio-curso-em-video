#Crie uma Tupla preenchida com os 20 Primeiros colocados
#da Tabela do Campeonato Brasileiro de Futebol, na ordem
#de colocação. Depois mostre:
#A) Apenas os 5 Primeiros colocados
#B) Os Últimos 4 colocados da tabela
#C) Uma lista com os times em ORDEM ALFABÉTICA
#D) Em que POSIÇÃO na tabela está o time da CHAPECOENSE
times = ('flamengo', 'internacional', 'atletico-mg', 'sao paulo', 'fluminense', 'gremio', 'palmeiras','santos','athletico-pr','bragantino','ceara','corinthia','atletico-go','bahia','spot recife','fortaleza','vasco da gama','goias','coritiba','botafogo')
print('A) Os 5 primeiros colocados')
for cont in range(0, 5):
    print(f'O time {times[cont]} está na {cont+1}ª colocação')
print('B) Os 4 últimos colocados')
for cont in range(15, 19):
    print(f'O time {times[cont]} está na {cont+1}ª colocação')
print('C) Uma lista em ordem alfabética')
print(sorted(times))
print('D) Chapecoense aparece?')
num = 0
valor = 0
for cont in range(0, len(times)):
    if times[cont] == 'chapecoense':
        valor = cont + 1
        num += 1
        break
if num == 1:
    print(f'Chapecoense classificada na {valor}ª posição')
else:
    print('Chapecoense não classificada')
print('Fim do Programa')