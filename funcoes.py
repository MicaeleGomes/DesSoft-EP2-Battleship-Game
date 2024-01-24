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
#EP2: Preenche Frota
def preenche_frota(dados_de_posicionamento, nome_navio, frota):
    posicoes_navio = define_posicoes(dados_de_posicionamento)
    
    nova_embarcacao = {
        "tipo": nome_navio,
        "posicoes": posicoes_navio
    }
    
    frota.append(nova_embarcacao)
    
    return frota
