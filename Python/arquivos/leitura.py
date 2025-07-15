"""
open()-> retorna um _io_TextIOWrapper
Por padrao, a funcao open() abre o arquivo para leitura
Se o arquivo nao existir erro FileNotFoundError

"""
arquivo = open('recursos/texto.txt')
print(arquivo)
print(type(arquivo))
print(arquivo.read())