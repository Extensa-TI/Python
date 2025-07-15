"""
listas = [[1,2,3],[4,5,6],[7,8,9]]

print(listas)
print(type(listas))
print(listas[0][1])

for lista in listas:
    for numero in lista:
        print(numero)

#Em list comprehesion
[[print(valor) for valor in lista] for lista in listas]

"""

# gerando um tabuleiro 3 x 3
tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

print([['*' for i in range(1,4)] for j in range(1,4)])
