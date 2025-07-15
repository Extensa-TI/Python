"""
A funcao reverse() so funciona em list
A funcao reversed() em todos iteraveis e retorna um objeto
List Reverse Iterator
"""

lista = [1,2,3,4,5]
res = reversed(lista)
print(lista)
print(res)
print(type(res))

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # em set nao definimos a ordem dos elementos

for letra in reversed('Geek University'):
    print(letra,end='')

print()
print(''.join(list(reversed('Geek University'))))
print('Geek University'[::-1])

for n in reversed(range(0,10)):
    print(n)

for n in range(9,-1,-1):
    print(n)