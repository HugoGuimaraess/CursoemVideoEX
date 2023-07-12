import random




print('Sou o computador....')
print('Será que voce consegue advinha qual número eu estou pensando de 0 a 10?')
maquina = random.randint(0,10)
cont = 0
while True:
    jogador = int(input('Qual seu palpite?'))
    cont += 1

    if jogador < maquina:
        print('O valor é Maior')
    elif jogador > maquina:
        print('O valor é Menor')
    elif jogador == maquina:
        break

print('Parabéns')
print('Você consegui acertar na {}º Tentativa, o valor era {}'.format(cont,maquina))