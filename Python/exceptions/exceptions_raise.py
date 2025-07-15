"""
Dica de quando e onde tratar codigo:
TODA ENTRADA DEVE SER TRATADA!

raise -> lanca uma execao

def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor {cor}')

colore('ola','azul')
colore('ola',1)
colore(1,'azul')
colore(1,2)

def colore(texto,cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores} cores')
    print(f'O texto {texto} sera impresso na cor {cor}')

colore('ola','azul')
colore('ola','preto')
"""





   
