from random import randint


def listar(lista):
    print('Sorteando 5 números aleatórios: ',end='')
    for c in range(0,5):
        a=randint(1,10)
        lista.append(a)
        print(f'{a} ',end='')
    print('Pronto!')



def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma = soma + c
    print(f'A soma dos números pares é {soma}')

def somaimpar(lista):
    sub=0
    for c in lista:
        if c % 2 == 1:
            sub += c
    print(f'A soma dos números impares é {sub}')


numero=list()

listar(numero)
somapar(numero)
somaimpar(numero)