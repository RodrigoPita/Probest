# bibliotecas complementares
from random import randint

# constante para simular infinitas iteracoes
TAM = 5000000

# funcoes complementares
def shiftR( L:list ) -> list:
    '''Recebe uma lista L e faz um shift de seus elementos para a direita
    ex. shiftR( [1, 2, 3] ) -> [3, 1, 2]'''
    if ( len( L ) <= 1 ): return L
    return [L[-1]] + L[:-1]

def shiftL( L:list ) -> list:
    '''Recebe uma lista L e faz um shift de seus elementos para a esquerda
    ex. shiftL( [1, 2, 3] ) -> [2, 3, 1]'''
    if ( len( L ) <= 1 ): return L
    return L[1:] + [L[0]]

# Questao 1
def posicao( inf:bool = False, t:int = TAM, L:list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ) -> list:
    '''Calcula a posicao de uma particula em relacao aos vertices do poligono p
    depois de passados t segundos, retornando uma nova lista com a posicao atual
    da particula ou uma lista com essa mesma nova lista e o tempo, caso todos
    os vertices tenham sido visitados'''
    # lista auxiliar para registrar quais vertices ja foram percorridos
    auxL = [] + L

    for i in range( t ):
        # variavel para indicar em qual sentido a particula vai se mover
        sinal = randint( 0, 1 )

        # caso o sinal seja 1, a particula anda no sentido horario
        if ( sinal ): L = shiftR( L )
        # caso o sinal seja 0, a a particula anda no sentido anti-horario
        else: L = shiftL( L )

        # posicao atual da particula
        pos = L.index( 1 )

        # se a particula estiver num vertice novo pela primeira vez, o vertice fica registrado na lista auxiliar
        if ( auxL[pos] < 1 ): auxL[pos] = 1
        else: auxL[pos] += 1 # caso a particula esteja revisitando o vertice, incrementamos o numero de visitas

        # se todos os vertices tiverem sido visitados, retorna o tempo em que isso ocorreu
        if ( 0 not in auxL and not inf ): return [ L, i ]
    return [ auxL, t ]

# Questao 2
def caso( s:str ) -> int:
    '''Calcula com igual probabilidade qual movimento o inseto deve fazer
    0 -> esquerda
    1 -> cima
    2 -> direita
    3 -> baixo
    '''
    # caso em que o inseto se encontra na posicao superior central do tabuleiro
    if ( s == '01' ):
        aux = [0, 2, 3]
        return aux[randint( 0, 2 )]
    # caso em que o inseto se encontra na posicao superior direita do tabuleiro
    elif ( s == '02' ):
        aux = [0, 3]
        return aux[randint( 0, 1 )]
    # caso em que o inseto se encontra na posicao central esquerda do tabuleiro
    elif ( s == '10' ):
        aux = [1, 2, 3]
        return aux[randint( 0, 2 )]
    # caso em que o inseto se encontra na posicao central do tabuleiro
    elif ( s == '11' ):
        aux = [0, 1, 2, 3]
        return aux[randint( 0, 3 )]
    # caso em que o inseto se encontra na posicao central direita do tabuleiro
    elif ( s == '12' ):
        aux = [0, 1, 3]
        return aux[randint( 0, 2 )]
    # caso em que o inseto se encontra na posicao inferior esquerda do tabuleiro
    elif ( s == '20' ):
        aux = [1, 2]
        return aux[randint( 0, 1 )]
    # caso em que o inseto se encontra na posicao inferior central do tabuleiro
    elif ( s == '21' ):
        aux = [0, 1, 2]
        return aux[randint( 0, 2 )]
    # caso de erro
    return -1

def imprimeTabuleiro( M:list ) -> None:
    '''Imprime o tabuleiro M em forma de matriz'''
    # imprime a borda superior do tabuleiro
    print( '\n' + '-'*13 )
    for i in M:
        # imprime as linhas do tabuleiro
        print( f'| {i[0]} | {i[1]} | {i[2]} |')
    # imprime a borta inferior do tabuleiro
    print( '-'*13 + '\n' )

def iteraSalto( M:list, trajeto:list = [] ) -> list:
    '''Entra num loop de iteracoes da funcao salto ate que o inseto caia na armadilha'''
    # inicializando variaveis auxiliares para nao alterar os valores originais
    auxM, auxTrajeto = [] + M, [] + trajeto
    while ( True ):
        auxM, auxTrajeto = salto( auxM, auxTrajeto )
        # quebra o loop caso o inseto seja capturado
        if ( 'armadilha' in auxTrajeto[-1] ): break
    return [ auxM, auxTrajeto ]

def iteraSalto2( M:list, trajeto:list = [], count:int = 0 ) -> list:
    '''Faz o mesmo que a funcao iteraSalto, mas tambem registra o numero count de vezes
    que o inseto visita a casa central'''
    # inicializando variaveis auxiliares para nao alterar os valores originais
    auxM, auxTrajeto, auxCount = [] + M, [] + trajeto, count
    while ( True ):
        auxM, auxTrajeto = salto( auxM, auxTrajeto )
        # incrementa a conta caso haja visita a casa central
        if ( auxM[1][1] == 1 ): auxCount += 1
        # quebra o loop caso o inseto seja capturado
        if ( 'armadilha' in auxTrajeto[-1] ): break
    return [ auxM, auxTrajeto, auxCount ]

def probabilidadeArmadilhas( casos:list ) -> list:
    '''A partir de uma lista casos, confere quantas vezes o inseto
    caiu na armadilha1 e na armadilha2, depois calcula a probabilidade
    de o inseto cair em cada uma, de acordo com os testes feitos'''
    # inicializando a lista com a contagem de capturas por armadilha e uma variavel para o total de casos
    contagemArmadilhas, total = [ 0, 0 ], len( casos )
    for i in casos:
        # incrementando o numero de capturas da armadilha1
        if ( 'armadilha1' in i ): contagemArmadilhas[0] += 1
        # incrementando o numero de capturas da armadilha2
        elif ( 'armadilha2' in i ): contagemArmadilhas[1] += 1
    # retornando uma lista com a probabilidade arredondada da captura de cada armadilha
    return [ round( contagemArmadilhas[0] * 100 / total, 2 ), round( contagemArmadilhas[1] * 100 / total, 2 ) ]

def salto( M:list, trajeto:list = []) -> list:
    '''Calcula a posicao de um inseto num tabuleiro M após um salto'''
    # dicionario para legenda das direcoes
    legenda = { 0: 'esquerda',
                1: 'cima',
                2: 'direita',
                3: 'baixo',
                4: 'armadilha1',
                5: 'armadilha2' }

    # o inseto ja se encontra na armadilha superior
    if ( M[0][0] == 1 ):
        # fecha a lista do trajeto
        if ( legenda[4] not in trajeto ): trajeto.append( legenda[4] )
        return [ M, trajeto ]
    # o inseto ja se encontra na armadilha inferior
    elif ( M[2][2] == 1 ):
        # fecha a lista do trajeto
        if ( legenda[5] not in trajeto ): trajeto.append( legenda[5] )
        return [ M, trajeto ]

    for i in range( 3 ):
        if ( 1 not in M[i] ): continue # pula a iteracao, caso o inseto nao esteja na linha i do tabuleiro
        for j in range( 3 ):
            # se o inseto estiver na posicao Mij do tabuleiro
            if ( M[i][j] == 1 ):
                # chama a funcao auxiliar caso para escolher a direcao do movimento do inseto
                dir = caso( str( i ) + str( j ) )
                trajeto.append( legenda[dir] ) # atualiza a lista do trajeto
                # esquerda
                if ( dir == 0 ):
                    M[i] = shiftL( M[i] )
                # cima
                elif (dir == 1 ):
                    M = shiftL( M )
                # direita
                elif (dir == 2 ):
                    M[i] = shiftR( M[i] )
                # baixo
                elif ( dir == 3 ):
                    M = shiftR( M )
                # caso de erro
                else: 
                    print( f'--ERRO {dir}, caso invalido--')
                    return -1
                return [ M, trajeto ]

def main():
    # numero de testes
    n1 = 5000
    n2 = 10000
    
    # lista de testes para quantos passos a particula leva ate visitar todos os vertices, ou seja, lista de Y
    q1Testes = [ posicao()[1] for i in range( n1 ) ]

    # 1.b) E[Y]
    espY = sum( q1Testes ) / len( q1Testes )

    print( f'O valor de E[Y] = {espY}\n' )

    # 1.d) chamar posicao() depois de um tempo TAM suficientemente grande
    Z, tempoTotal = posicao( True )

    print( f'A massa de probabilidade da variável Z se dá por:' )
    for i in range( len( Z ) ):
        # calculando a probabilidade da particula estar em cada vertice
        aux = round( Z[i] / tempoTotal * 100, 2 )
        print( f' -Vertice {i}: {aux} %' )

    # tabuleiro com o inseto na posicao inicial
    caso_01 = [ [0, 1, 0], [0, 0, 0], [0, 0, 0] ]
    caso_02 = [ [0, 0, 1], [0, 0, 0], [0, 0, 0] ]
    caso_10 = [ [0, 0, 0], [1, 0, 0], [0, 0, 0] ]
    caso_11 = [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]
    caso_12 = [ [0, 0, 0], [0, 0, 1], [0, 0, 0] ]
    caso_20 = [ [0, 0, 0], [0, 0, 0], [1, 0, 0] ]
    caso_21 = [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ]

    # 2.c) testes com os trajetos ate a armadilha, especificando qual das duas armadilhas
    armadilhas_01 = [ iteraSalto( caso_01 )[1] for i in range( n2 ) ]
    armadilhas_02 = [ iteraSalto( caso_02 )[1] for i in range( n2 ) ]
    armadilhas_10 = [ iteraSalto( caso_10 )[1] for i in range( n2 ) ]
    armadilhas_11 = [ iteraSalto( caso_11 )[1] for i in range( n2 ) ]
    armadilhas_12 = [ iteraSalto( caso_12 )[1] for i in range( n2 ) ]
    armadilhas_20 = [ iteraSalto( caso_20 )[1] for i in range( n2 ) ]
    armadilhas_21 = [ iteraSalto( caso_21 )[1] for i in range( n2 ) ]
    
    # probabilidades de o inseto ser capturado por cada uma das armadilhas para cada caso
    probs_armadilhas_01 = probabilidadeArmadilhas( armadilhas_01 )
    probs_armadilhas_02 = probabilidadeArmadilhas( armadilhas_02 )
    probs_armadilhas_10 = probabilidadeArmadilhas( armadilhas_10 )
    probs_armadilhas_11 = probabilidadeArmadilhas( armadilhas_11 )
    probs_armadilhas_12 = probabilidadeArmadilhas( armadilhas_12 )
    probs_armadilhas_20 = probabilidadeArmadilhas( armadilhas_20 )
    probs_armadilhas_21 = probabilidadeArmadilhas( armadilhas_21 )

    # lista auxiliar com as probabilidades de cada caso
    probs_armadilhas = [ [ probs_armadilhas_01, '01' ], 
                         [ probs_armadilhas_02, '02' ], 
                         [ probs_armadilhas_10, '10' ], 
                         [ probs_armadilhas_11, '11' ], 
                         [ probs_armadilhas_12, '12' ], 
                         [ probs_armadilhas_20, '20' ], 
                         [ probs_armadilhas_21, '21' ], ]

    print( f'\nProbabilidades do inseto ser capturado por cada armadilha:' )
    for i in probs_armadilhas: 
        print( f' -Caso {i[1]}:' )
        for j in i[0]: print( f'  -Armadilha {i[0].index( j ) + 1}: {j} %' )

    # 2.d) testes do numero de saltos ate a armadilha para cada caso de posicao inicial do inseto
    t01 = [ len( iteraSalto( caso_01 )[1] ) for i in range( n2 ) ]
    t02 = [ len( iteraSalto( caso_02 )[1] ) for i in range( n2 ) ]
    t10 = [ len( iteraSalto( caso_10 )[1] ) for i in range( n2 ) ]
    t11 = [ len( iteraSalto( caso_11 )[1] ) for i in range( n2 ) ]
    t12 = [ len( iteraSalto( caso_12 )[1] ) for i in range( n2 ) ]
    t20 = [ len( iteraSalto( caso_20 )[1] ) for i in range( n2 ) ]
    t21 = [ len( iteraSalto( caso_21 )[1] ) for i in range( n2 ) ]

    # media de saltos do inseto, para cada caso, ate que ele chegue numa armadilha
    media01 = sum( t01 ) / len( t01 )
    media02 = sum( t02 ) / len( t02 )
    media10 = sum( t10 ) / len( t10 )
    media11 = sum( t11 ) / len( t11 )
    media12 = sum( t12 ) / len( t12 )
    media20 = sum( t20 ) / len( t20 )
    media21 = sum( t21 ) / len( t21 )

    print( f'\nMédias de saltos são:\n ' +
           f'-Caso 01: {media01}\n ' +
           f'-Caso 02: {media02}\n ' +
           f'-Caso 10: {media10}\n ' +
           f'-Caso 11: {media11}\n ' +
           f'-Caso 12: {media12}\n ' +
           f'-Caso 20: {media20}\n ' +
           f'-Caso 21: {media21}\n' )
    
    # 2.e) lista de testes para a posicao inferior esquerda, considerando o numero de visitas a casa central
    t20_2 = [ iteraSalto2( caso_20 )[2] for i in range( n2 ) ]
    
    # media de vezes que o inseto visita a casa central antes de ser capturado
    media20_2 = sum( t20_2 ) / len( t20_2 )

    print( f'O inseto, em média, visita o centro {media20_2} vezes antes de ser capturado.')

main()
