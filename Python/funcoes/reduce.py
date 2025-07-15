"""

"""
from functools import reduce

dados = [2,3,4,5,7,11,13,17,19,23,29]

print('Para utilizar o reduce precisamos de uma funcao que receba dois parametros')
multi = lambda x,y: x * y
result = reduce(multi,dados)
print(result)

print()
print('Utilizando um loop normal')
res = 1
for n in dados:
    res = res * n

print(res)
