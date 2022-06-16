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
    da particula'''
    auxL = [] + L # lista para registrar quais vertices ja foram percorridos
    if ( t == 0 ):
        return [t, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # inicializando os vertices do poligono com a particula na posicao inicial

    for i in range( t ):
        sinal = randint( 0, 1 ) # variavel para indicar em qual sentido a particula vai se mover
        if ( sinal ): L = shiftR( L )
        else: L = shiftL( L )
        auxI = L.index( 1 )
        if auxL[auxI] != 1: auxL[auxI] = 1
        if ( 0 not in auxL ): return( i )

def main():
    print( posicao( 7, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ) )

main()