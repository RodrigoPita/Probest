# bibliotecas complementares
import io

FILE_NAME = 'zipf.txt'

def get_data_from_file( file_name:str ) -> list:
    '''Abre um arquivo e coloca todo o seu conteudo em uma string'''
    file_content = ''
    for line in io.open( file_name, mode = 'r', encoding = 'utf-8' ):
        file_content += line
    return file_content

def format_string( string:str ) -> str:
    '''Formata uma string, tirando todos os simbolos sem ser carateres do alfabeto padrao'''
    formated_string = string.strip().replace( ',', '' ).replace( '.', '' ).replace( ';', '' ).replace( '(', '' ).replace( ')', '' ).replace( '\n', '' )
    return formated_string

def count_frequency( text:str ) -> dict:
    '''Conta a frequencia de ocorrencias de cada palavra num texto,
    retornando um dicionario com as palavras e suas respectivas ocorrencias'''
    