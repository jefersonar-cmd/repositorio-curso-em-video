#criar um programa que tenha uma Tupla totalmente preenchida
#com uma contagem por extenso, de ZERO até VINTE

#Seu programa deverá ler um número pelo teclado
#(entre 0 e 20) e mostrá-la por extenso
extenso = ('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    valor = int(input('Digite um valor (de 0 à 20): '))
    if valor >= 0 and valor <= 20:
        print(f'O valor {valor} por extenso é {extenso[valor]}')
        break
    else:
        print(f'Número {valor} inexistente')
        continue