nome = str(input('Nome do Jogador:'))
partidas = int(input('Quantas partidas {} jogou?'.format(nome)))
lista_gols=[]

for c in range(0,partidas):
    qnt_gol = int(input('Quantos Gols na partida {}?'.format(c+1)))
    lista_gols.append(qnt_gol)
dic_dados = {'nome':nome,'partidas':partidas,'gols':lista_gols}

print('=-'*30)
print(dic_dados)
print('=-'*30)
print('O campo NOME tem o valor {}'.format(nome))
print('O campo PARTIDAS tem o valor {}'.format(partidas))
print('O campo GOLS tem o valor {}'.format(lista_gols))

print('=-'*30)
print('O jogador {} jogou {} partidas:'.format(nome,partidas))
for v in range(0,partidas):
    print('=> Na partida {}, fez {}'.format(v,lista_gols[v]))
print('Foi um total de {} gols'.format(sum(lista_gols)))
print('O maior número de gols foi {}'.format(max(lista_gols)))
print('O menor número de gols foi {}'.format(min(lista_gols)))




#for k,j in dic_dados.items():
#    print('O campo {} tem valor {}'.format(k,j))