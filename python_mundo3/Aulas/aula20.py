def lin():
    print('-'*30)


lin()
print('        CURSO EM VIDEO')
lin()

# função super personalizada
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('          Hello World!')
# parte "prática"


def soma(a, b):
    s = a + b
    print(s)


soma(8, 9)
# função com muitos valores


def contador(*num):
    print(len(num))


contador(2,3,4,1,2)
# função com listas

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [2,3,4,5,8]
dobra(valores)
print(valores)