from time import sleep



def maior(*lista):
    listando=[]
    print('Analisando valores: ',end='')
    for c in lista:
        sleep(0.3)
        print(f'{c}, ', end='')
        listando.append(c)
    if len(listando)== 0:
        print('Não teve valores para analisar, ', end='')
        print('O maior valor foi 0\n')
    else:
        print(f'O maior valor foi {max(listando)}\n')




maior(1,3,4,5,8)
maior(1,3,4)
maior()
maior(5,2,7,9,10)
