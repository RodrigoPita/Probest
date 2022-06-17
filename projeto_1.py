# bibliotecas complementares
from random import randint

# funcoes complementares
def shiftR( L:list ) -> list:
    '''Recebe uma lista L e faz um shift de seus elementos para a direita
    ex. shiftR( [1, 2, 3] ) -> [3, 1, 2]'''
    
    if len( L ) <= 1:
        return L
    return [L[-1]] + L[:-1]

def shiftL( L:list ) -> list:
    '''Recebe uma lista L e faz um shift de seus elementos para a esquerda
    ex. shiftL( [1, 2, 3] ) -> [2, 3, 1]'''
    
    if len( L ) <= 1:
        return L
    return L[1:] + [L[0]]

# Questao 1

def posicao( t:int, L:list ) -> list:
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
        if ( auxL[pos] != 1 ): auxL[pos] = 1

        # se todos os vertices tiverem sido visitados, retorna o tempo em que isso ocorreu
        if ( 0 not in auxL ): return [L, i]
    return L

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
    print( '\n' + '-'*13 )
    for i in M:
        print( f'| {i[0]} | {i[1]} | {i[2]} |')
    print( '-'*13 + '\n' )

def salto( M:list, trajeto = []) -> list:
    '''Calcula a posicao de um inseto num tabuleiro M após um salto'''

    # dicionario para legenda das direcoes
    legenda = { 0: 'esquerda',
                1: 'cima',
                2: 'direita',
                3: 'baixo',
                4: 'armadilha' }

    # o inseto ja se encontra numa armadilha
    if ( M[0][0] == 1 or M[2][2] == 1 ):
        if ( legenda[4] not in trajeto ): trajeto.append( legenda[4] ) # fecha a lista do trajeto
        return [ M, trajeto ]
    for i in range(3):
        if ( 1 not in M[i] ): continue # pula a iteracao, caso o inseto nao esteja na linha i do tabuleiro
        for j in range(3):
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
    # lista dos vertices com a particula na posicao inicial
    L = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # numero de testes
    n = 5000
    
    # lista de testes para quantos passos a particula leva ate visitar todos os vertices, ou seja, lista de Y
    testes = [ posicao( 10000, L )[1] for i in range( n ) ]

    # E[Y]
    espY = sum( testes ) / len( testes )
    print( f'O valor de E[Y] = {espY}' )

    # tabuleiro com o inseto na posicao inicial
    M = [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]
    imprimeTabuleiro( M )
    M, trajeto = salto( M )
    imprimeTabuleiro( M )
    M, trajeto = salto( M, trajeto )
    imprimeTabuleiro( M )
    M, trajeto = salto( M, trajeto )
    imprimeTabuleiro( M )
    print( trajeto )

main()