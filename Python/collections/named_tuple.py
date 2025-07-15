"""
Módulo Collection - Named Tuple
"""
from collections import namedtuple

# Declaração forma 1
cachorro = namedtuple('cachorro','idade raca nome')

# Declaração forma 2
cachorro = namedtuple('cachorro', 'idade,raca,nome')

# Declaração forma 2
cachorro = namedtuple('cachorro', ['idade','raca','nome'])

ray = cachorro(2, 'Chow Chow', 'Ray')
print(ray)
print(type(ray))
# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])
# Forma2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow Chow'))
print(ray.count('Chow Chow'))
