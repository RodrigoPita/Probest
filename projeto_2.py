# bibliotecas complementares
import io
import matplotlib.pyplot as plt
import numpy as np

FILE_NAME = 'zipf.txt'

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

def main():
    text = get_data_from_file( FILE_NAME )
    formated_text = format_string( text )
    frequencies = count_frequency( formated_text )
    plot_frequencies( frequencies )

main()