"""
List Comprehension

numeros = [1,2,3,4,5]
res = [numero * 10 for numero in numeros]
print(res)

res =[numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor ** 2

res = [funcao(numero) for numero in numeros]
print(res)

nome = 'Geek University'
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])

print([numero * 3 for numero in range(1,10)])

print([bool(valor) for valor in [0,[],'',True,1, 3.14]])

print([str(numero) for numero in [1,2,3,4,5]])

numeros = [1,2,3,4,5,6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)
"""

numeros = [1,2,3,4,5,6]

res = [numero * 2 if not numero % 2 else numero /2 for numero in numeros]
print(res)

