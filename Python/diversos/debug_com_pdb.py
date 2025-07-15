"""
PDB -> Python Debugger

comandos basicos do pdb:
l -> listar onde estamos no código
n -> próxima linha
p -> imprime variável
c -> continua a execução - finaliza o debugging

Exemplo 1:
import pdb;

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

Exemplo 2:

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace() 
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

Porque utilizar neste formato?
1. O debug é utilizado durante o desenvolvimento. Costumamos realizar os imports 
de bibliotecas no início do arquivo.
2. Não faz sentido colocar esse import junto com os outros.

A partir do Python 3.7 nao e mais necessario importar a biblioteca pdb, pois o comando de debug
foi incorporado como funcao built-in do Python chamada breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint() 
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
Exemplo:
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

Como os nomes das variaveis sao igual aos comandos do pdb, devemos utilizar o comando p para imprimir
as variaveis, pois se utilizarmos os comandos n, l, c, o pdb ira executar o comando e nao a variavel.
"""


 



