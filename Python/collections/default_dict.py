"""
Módulo Collections -> Default Dict
"""
from collections import defaultdict

dicionario = defaultdict(lambda:0)
dicionario['curso'] = 'Programção em Python: Essencial'
print(dicionario)

print(dicionario['outro']) # não gera o keyError e preenche o dicionário com a chave outro e o valor 0
print(dicionario) 

