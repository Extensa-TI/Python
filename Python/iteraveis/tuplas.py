print(type(()))
tupla1 = (1,2,3,4)
print(tupla1)

tupla2 = 1,2,3,4,5,6
print(tupla2)

# tuplas de 1 elemento
tupla3 = (4) # isso não pe uma tupla, é um int
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # issto é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

tupla = tuple(range(11))
print(tupla)

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

# sum()
tupla = (1,2,3,4,5,6)
print(sum(tupla))

# max()
print(max(tupla))

# min()
print(min(tupla))

# len()
print(len(tupla))

# concatenação de tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
print(tupla1)
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

# in
print(3 in tupla)

# iterando
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice,valor)

# count()
tupla =('a', 'b','c','d','e','a','b')
print(tupla.count('a'))

# index()
print(tupla.index('a'))
print(tupla.index('a',1))

# slicing
print(tupla[0:])
print(tupla[3:6])
print(tupla[0::2])

# copiando tuplas
nova = (4,5,6)
outra = tupla + nova
print(outra)
