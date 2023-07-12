def jogador(nome,gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'o jogador {nome} fez {gols} gols  no campeonato')


jogador(nome=str(input('Nome do jogaodr: ')),gols=str(input('Quantos gols: ')))
