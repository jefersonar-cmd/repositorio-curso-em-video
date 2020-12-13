#aula 9

frase = str('Curso em Vídeo Python')
print(len(frase)) #conta os caracteres e o espacos
print(frase[4:13]) #comeca em 1 e termina em outro
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")
print(frase.count('o')) #conta quantos O's tem
print(frase.upper().count('O')) #contando quantos O's jogados para maiúsculos na frase.
print(len(frase.strip())) #conta os numero de caracter sem os espacos adicionais
print(frase.replace('Python', 'Android')) #substitui palavas
print(frase.lower()) #diminui
print(frase.upper()) #maxmiza
print(frase.capitalize()) #deixa a pimeira letra em caps
print('Curso' in frase) #verifica se os caracteres está no string
dividido = frase.split() #divide as palavras em array
print(dividido)
print(dividido[0])
print(dividido[0][2])

