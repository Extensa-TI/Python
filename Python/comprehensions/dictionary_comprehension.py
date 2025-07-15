"""
numeros = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
quadrado = {chave:valor ** 2 for chave,valor in numeros.items()}
print(quadrado)

numeros = [1,2,3,4,5,1,2]
quadrado = {valor:valor ** 2 for valor in numeros}
print(quadrado)

chave = 'abcde'
numeros = [1,2,3,4,5]
mistura = {chave[i]:numeros[i] for i in range(0, len(chave))}
print(mistura)

"""
numeros = [1,2,3,4,5]
res = {nun:('par' if nun % 2 == 0 else 'impar') for nun in numeros}
print(res)
