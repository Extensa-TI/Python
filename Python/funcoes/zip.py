"""
 Cria um iteravel que agrega elementos de cada um dos iteraveis passados como argumento.

 lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = ['a', 'b', 'c']

zip1 = zip(lista1, lista2, lista3)
print(type(zip1))
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
zip1 = zip(lista1, lista2, lista3)
print(tuple(zip1))
zip1 = zip(lista1, lista2, lista3)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

lista4 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista4)

print(list(zip1))

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
"""

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
