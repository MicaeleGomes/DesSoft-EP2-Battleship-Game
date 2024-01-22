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

print(posiciona_frota([
  { "tipo": "porta-aviões", "posicoes": [[1, 5], [1, 6], [1, 7], [1, 8]]},
  { "tipo": "navio-tanque", "posicoes": [[4, 7], [5, 7], [6, 7]]},
  { "tipo": "navio-tanque", "posicoes": [[6, 1], [6, 2], [6, 3]]},
  { "tipo": "destroyer", "posicoes": [[1, 1], [2, 1]]},
  { "tipo": "destroyer", "posicoes": [[2, 3], [3, 3]]},
  { "tipo": "destroyer", "posicoes": [[9, 1], [9, 2]]},
  { "tipo": "submarino", "posicoes": [[0, 3]]},
  { "tipo": "submarino", "posicoes": [[4, 5]]},
  { "tipo": "submarino", "posicoes": [[8, 4]]},
  { "tipo": "submarino", "posicoes": [[8, 9]]}
  ]))

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
            
print(afundados([
  { "tipo": "porta-aviões", "posicoes": [[1, 5], [1, 6], [1, 7], [1, 8]]},
  { "tipo": "navio-tanque", "posicoes": [[4, 7], [5, 7], [6, 7]]},
  { "tipo": "navio-tanque", "posicoes": [[6, 1], [6, 2], [6, 3]]},
  { "tipo": "destroyer", "posicoes": [[1, 1], [2, 1]]},
  { "tipo": "destroyer", "posicoes": [[2, 3], [3, 3]]},
  { "tipo": "destroyer", "posicoes": [[9, 1], [9, 2]]},
  { "tipo": "submarino", "posicoes": [[0, 3]]},
  { "tipo": "submarino", "posicoes": [[4, 5]]},
  { "tipo": "submarino", "posicoes": [[8, 4]]},
  { "tipo": "submarino", "posicoes": [[8, 9]]}
], [
  [0, '-', '-',  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
  [0,  1 ,  0 ,  0 ,  0 , 'X', 'X', 'X', 'X',  0 ],
  [0,  1 ,  0 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
  [0,  0 ,  0 ,  1 , '-', '-', '-', '-',  0 ,  0 ],
  [0, '-',  0 ,  0 ,  0 ,  1 ,  0 ,  1 ,  0 ,  0 ],
  [0,  0 ,  0 ,  0 , '-',  0 ,  0 ,  1 ,  0 ,  0 ],
  [0,  1 ,  1 ,  1 ,  0 ,  0 ,  0 ,  1 ,  0 ,  0 ],
  [0,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ],
  [0,  0 ,  0 ,  0 , 'X',  0 ,  0 ,  0 ,  0 ,  1 ],
  [0,  1 ,  1 , '-', '-', '-', '-', '-', '-', '-']
]))

