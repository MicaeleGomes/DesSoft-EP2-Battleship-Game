#EP2:Define posições

def define_posicoes(dados_de_posicionamento):
    linha = dados_de_posicionamento["linha"]
    coluna = dados_de_posicionamento["coluna"]
    orientacao = dados_de_posicionamento["orientacao"]
    tamanho = dados_de_posicionamento["tamanho"]
    
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
            
    return posicoes

def posiciona_frota(lista_frota):
    #crio um tabuleiro 10 x 10
    grid = [[0] * 10 for _ in range(10)]
    # acessando cada avião
    for frota in lista_frota:
        #acessando, no avião, a sua posição
        lista_posicao = frota['posicoes']
        #atualizando as posicoes no tabuleiro por 1
        for y_x in lista_posicao:
            posicao_em_y = y_x[0]
            posicao_em_x = y_x[1]
            grid[posicao_em_y][posicao_em_x] = 1
        
    return grid

def afundados(lista_frota,situacao_atual):
    afundado = 0
    for frota in lista_frota:
        lista_posicao = frota['posicoes']
        parte_achada = 0
        for y_x in lista_posicao:
            posicao_em_y = y_x[0]
            posicao_em_x = y_x[1]
            if situacao_atual[posicao_em_y][posicao_em_x] == 'X':
                parte_achada += 1
        if parte_achada == len(lista_posicao):
            afundado += 1
            parte_achada = 0
        else:
            parte_achada = 0
    return afundado

