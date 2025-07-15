"""
Para ler o u escrever dados em arquivos do sistema operacional o
software precisa ter permissao.

StringIO-> Utilizado para ler e criar arquivos na memoria
"""
from io import StringIO

mensagem = 'Esta e apenas uma string normal\n'

arquivo = StringIO(mensagem)
print(arquivo.read())
arquivo.write('Outro texto\n')
arquivo.seek(0)
print(arquivo.read())

