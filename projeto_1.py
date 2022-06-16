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

def posicao( t:int, L:list ) -> int or tuple:
    '''Calcula a posicao de uma particula em relacao aos vertices do poligono p
    depois de passados t segundos, retornando uma nova lista com a posicao atual
    da particula'''
    
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
        if auxL[pos] != 1: auxL[pos] = 1

        # se todos os vertices tiverem sido visitados, retorna o tempo em que isso ocorreu
        if ( 0 not in auxL ): return( i )
    return (L, auxL)

def main():
    # lista dos vertices com a particula na posicao inicial
    L = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # numero de testes
    n = 100
    
    # lista de testes para quantos passos a particula leva ate visitar todos os vertices
    testes = [ posicao( 1000, L ) for i in range( n ) ]

    print( testes )
main()