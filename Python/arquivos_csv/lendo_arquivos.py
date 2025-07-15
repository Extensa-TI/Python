"""
CSV -> Comma Separated Values

# Possível de trabalhar mais não é o ideal
with open('diversos/lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

"""

# Duas formas para ler arquivos csv
# reader-> Permite iterar sobre a linhas do arquivo CSV como listas
# DictReader-> Permite iterar sobre as linhas do arquivo CSV como OrderedDict

from csv import reader

with open('recursos/lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # tira o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')

print()
from csv import DictReader

with open('recursos/lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # o parâmetro delimiter é opcional o delfult é vírbula
    for linha in leitor_csv:
        print(f"{linha['Nome']} nascem no(a) {linha['Pais']} e mede {linha['Altura (em cm)']} centimetros")


