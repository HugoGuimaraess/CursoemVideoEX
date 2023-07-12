

from time import sleep


def criararquivo(nome):
    try:
        a= open(nome,'wt+')
        a.close()
    except:
        print('erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')



def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('erro ao ler arquivo')
    else:
        print('pessoas cadastradas')
        print(a.read())

def cadastrar(arq,idade,nome):
    try:
        a=open(arq,'at')
    except:
        print('erro ao ler arquivo')
    else:
        a.write(f'idade: {nome} nome: {idade}')











def menu():
    print('-'*40)
    print('MENU PRINCPAL'.center(40))
    print('-'*40)
    print('\033[1;33m1 - ', end='')
    print('\033[1;34mVer pessoas cadastradas')
    print('\033[1;33m2 - ', end='')
    print('\033[1;34mCadastrar nova pessoa')
    print('\033[1;33m3 - ', end='')
    print('\033[1;34mSair do sistema\033[0;0m')
    print('-' * 40)









criararquivo('pessoas')
while True:

    menu()
    n = str(input('numero'))
    print('-' * 40)
    if n == '':
        print('opção inválida, programa encerrado')
        break
    elif n.isalpha():
        print('deve ser um valor númerico de 1 a 3')
        n = str(input('numero'))
    elif n.isnumeric():
        n=int(n)

        while True:
            if n>4 or n<= 0:
                print('erro, digite novamente')
            elif n ==1:
                print('opcao 1')
                lerarquivo('pessoas')
                break

            elif n == 2:
                print('opcao 2')
                nome = str(input('nome'))
                idade = int(input('idade'))
                cadastrar('pessoas',nome,idade)


                break
            elif n == 3:
                print('opcao 3')
                print('saindo do sistema')
                break

    if n == 3:
        break

