# bibliotecas complementares
import io
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math

FILE_NAME = 'zipf.txt'
TAM = 1000000

def get_data_from_file( file_name:str ) -> list:
    '''Abre um arquivo e coloca todo o seu conteudo em uma string'''
    file_content = ''
    for line in io.open( file_name, mode = 'r', encoding = 'utf-8' ):
        file_content += line
    return file_content

def format_string( string:str ) -> str:
    '''Formata uma string, tirando todos os simbolos sem ser carateres do alfabeto padrao'''
    formated_string = string.strip().replace( ',', '' ).replace( '.', '' ).replace( ';', '' ).lower()
    return formated_string.replace( '(', '' ).replace( ')', '' ).replace( ':', '' ).replace( '\n', '' )

def count_frequency( text:str ) -> dict:
    '''Conta a frequencia de ocorrencias de cada palavra num texto,
    retornando um dicionario com as palavras e suas respectivas ocorrencias'''
    all_words = text.split()
    frequency_by_word = {}
    for word in all_words:
        if ( frequency_by_word.get( word ) is not None ):
            frequency_by_word[word] += 1
        else: frequency_by_word[word] = 1
    return frequency_by_word

def plot_frequencies( freqs:dict ) -> None:
    '''Plota um grafico de acordo com as frequencias do dicionario dado'''
    aux = list( freqs.items() )
    elements = sorted( aux, key = lambda x: x[1], reverse = True )
    words = [ element[0] for element in elements ]
    occurences = [ element[1] for element in elements ]
    x_pos = np.arange( len( words ) )
    
    plt.title( 'Distribuição de Zipf no Projeto' )
    plt.plot( x_pos, occurences, linewidth = 2, color = 'r' )
    plt.bar( x_pos, occurences, align = 'center' )
    plt.xlabel( 'Palavras' )
    plt.ylabel( 'Ocorrências' )
    plt.show()

def list_of_Ys( const:int ) -> list:
    '''Cria uma lista de variaveis aleatorias Y'''
    low = 0
    high = 1/20
    Y = np.random.uniform( low, high, size = const )
    return Y

def mean_y( Y:list ) -> float:
    '''Valor esperado de Y'''
    n = len( Y )
    mean = sum( Y ) / n
    return mean

def g( y:float ) -> float:
    '''Funcao g(y)'''
    ans = 1 / ( 20 * ( y ** 2 ) * math.sqrt( 2 * math.pi ) ) * ( math.e ** ( -1 / ( 2 * y ** ( 2 ) ) ) )
    return ans

def mean_g( Y:list ) -> float:
    '''Valor esperado de g'''
    G = []
    for yi in Y:
        gi = g( yi )
        G.append( gi )
    n = len( G )
    mean = sum( G ) / n
    return mean

def main():
    # text = get_data_from_file( FILE_NAME )
    # formated_text = format_string( text )
    # frequencies = count_frequency( formated_text )
    # plot_frequencies( frequencies )

    Ys = list_of_Ys( TAM )
    E_y = mean_y( Ys )
    E_g = mean_g( Ys )
    print( f' -> E[Y] = {E_y}\n -> E[g(y)] = {E_g}')

main()