import random
itens=['Pedra','Papel','Tesoura']
print('Eu sou o computador e voce vai jogar contra mim ....')
print('Vamos jogar Pedra, Papel ou Tesoura')
print('[0] Pedra \n[1] Papel \n[2] Tesoura\n')


while True:
    computador = random.randint(0, 2)
    a = int(input('Escolha sua opção: '))

    if a < 0 or a > 2:
        print('apenas números válidos ')
        a = int(input('Escolha sua opção: '))

    else:
        print('Computador jogou {}'.format(itens[computador]))
        print('Computador jogou {}'.format(itens[a]))
        if computador == a:
            print('Empate, Vamos Novamente...')

        elif computador == 1:
            if a == 0:
                print('Você Perdeu')
                break
            elif a == 2:
                print('Você Ganhou')
                break
        elif computador == 2:
            if a == 0:
                print('Você Ganhou')
                break
            elif a == 1:
                print('Você Perdeu')
                break
        elif computador == 0:
            if a == 2:
                print('Você Perdeu')
                break
            elif a == 1:
                print('Você Ganhou')
                break

