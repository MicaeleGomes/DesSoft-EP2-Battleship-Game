import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!
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

def posicao_valida(dados_de_posicionamento,lista_frota):
    #imprimindo a posição desejada pelo jogador
    posicao_desejada = define_posicoes(dados_de_posicionamento)
    if lista_frota == []:
    #acessando a posicao desejada
        for posicao in posicao_desejada:
        #verificando se a posicao desejada está no limite
            if posicao[0] >= 10 or posicao[1] >= 10:
                return False
    
    else: 
        #acessado a posicao utilizada pela frota
        for embarcacao in lista_frota:
            posicao_embarcacao = embarcacao['posicoes']
            #acessando a posicao desejada
            for posicao in posicao_desejada:
                #verificando se a posicao desejada está no limite
                if posicao[0] >= 10 or posicao[1] >= 10:
                    return False
                #verificado se a posicao desejada está sendo usada
                elif posicao in posicao_embarcacao:
                    return False
    #se sair do loop, todos os casos estão disponiveis para uso
    return True
            
def preenche_frota(dados_de_posicionamento, nome_navio, frota):
    posicoes_navio = define_posicoes(dados_de_posicionamento)
    
    nova_embarcacao = {
        "tipo": nome_navio,
        "posicoes": posicoes_navio
    }
    
    frota.append(nova_embarcacao)
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

# criando uma lista de coordenadas já informadas pelo jogador
lista_coordenadas_informadas = []

while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # definindo um loop para as jogadas que ocorrerão dentro do loop jogando
    rodada = True
    while rodada:
        #lista de coordenana informada na rodada, a ser atualizada com a linha e coluna informada na jogada
        coordenada_informada = []
        # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
        ataque_linha = int(input('em qual linha você deseja atacar? '))
        while ataque_linha > 9 or ataque_linha < 0:
            print('Linha inválida!')
            ataque_linha = int(input('em qual linha você deseja atacar? '))
        # se sair do loop de ataque linha, append na coordenada informada com o ataque validado
        coordenada_informada.append(ataque_linha)
        # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
        ataque_coluna = int(input('em qual coluna você deseja atacar? '))
        while ataque_coluna > 9 or ataque_coluna < 0:
            print('Coluna inválida!')
            ataque_coluna = int(input('em qual coluna você deseja atacar? '))
        # se sair do loop de ataque coluna, append na coordenada informada com o ataque validado
        coordenada_informada.append(ataque_coluna)
        # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
        #verificando se a coordenada já foi informada pelo jogador
        if coordenada_informada not in lista_coordenadas_informadas:
            lista_coordenadas_informadas.append(coordenada_informada)
            jogada = faz_jogada(tabuleiro_oponente,ataque_linha,ataque_coluna)
            # finaliza a rodada
            rodada = False
        else:
            print(f'A posição linha {ataque_linha} e coluna {ataque_coluna} já foi informada anteriormente!')
            rodada = True
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
    jogo_atualizado = afundados(frota_oponente,tabuleiro_oponente)
    if jogo_atualizado == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        jogando = True