import random
import funcoes

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

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

            while not funcoes.posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            funcoes.preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = funcoes.posiciona_frota(frota_jogador)
tabuleiro_oponente = funcoes.posiciona_frota(frota_oponente)

jogando = True

# criando uma lista de coordenadas já informadas pelo jogador
lista_coordenadas_informadas = []

while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    #definindo um loop para as jogadas que ocorrerão dentro do loop jogando
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
            jogada = funcoes.faz_jogada(tabuleiro_oponente,ataque_linha,ataque_coluna)
            # finaliza a rodada
            rodada = False
        else:
            print(f'A posição linha {ataque_linha} e coluna {ataque_coluna} já foi informada anteriormente!')
            jogando = True
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
    jogo_atualizado = funcoes.afundados(frota_oponente,tabuleiro_oponente)
    if jogo_atualizado == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        jogando = True