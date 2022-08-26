#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
continuar = "S"
cinco = 'N'
while continuar == "S":
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = str(input("Deseja continuar?\n[S/N]: "))
    continuar = continuar.upper()
    if continuar == "N":
        break
    else:
        continue
print('=-'*31)
print(f'A) Foram digitados {len(lista)} números.')
print('=-'*31)
ListaDesc = lista.sort(reverse=True)
print('B) Lista de valores, ordenada de forma decrescente:')
for p, l in enumerate(lista):
    print(f'Valor: {l} e sua posição: {p}')
    if l == 5:
        cinco = 'S'
print('=-'*31)
if cinco == 'S':
    print('C) o valor 5 está na lista.')
elif cinco == 'N':
    print('C) O valor 5 não está na lista.')
