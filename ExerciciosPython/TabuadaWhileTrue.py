
while True:
    a = int(input('Digite um valor que queira ver a tabuada = '''))
    if a < 0:
        break
    else:
        for c in range(1,11):
            resultado = a * c
            print('{} x {} = {}'.format(a,c,resultado))

    print('Para parar o programa de tabuada digite um numero negativo.')