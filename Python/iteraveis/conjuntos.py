# definição
s = set({1,2,3,4,5,6,7, 6, 5, 4, 2})
print(s)
print(type(s))

s = {1,2,3,4,5,5,5}
print(s)

s = set('Geek University')
print(s)

lista = [1,2,3,4,5,6,7,6,5,4,3,2,1]
print(set(lista))

# in
s = {1,2,3,4,5,5,5}

if 3 in s:
    print('Têm o 3')
else:
    print('Não têm o 3')

# os elementos não são ordenados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f' Lista:  {lista} com {len(lista)} elementos')
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34)
print(f' Tupla:  {tupla} com {len(tupla)} elementos')
dicionario = {}.fromkeys(lista, 'dict')
print(f' Dicionário:  {dicionario} com {len(dicionario)} elementos')
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(f' Conjunto:  {conjunto} com {len(conjunto)} elementos')

# elementos misturados
s = {2, 'a', True, 3.84, 44}
print(s)

# interar
for valor in s:
    print(valor)

# utilização
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))
print(len(set(cidades)))

# add
s = {1,2,3}
s.add(4)
print(s)

# remove
s.remove(3)  # se o valor não for encontrado gera keyerror
print(s)

# discard
s.discard(1) # se o valor não for encontrado não gera erro
print(s)

s = {1,2,3}
novo = s.copy() #Deep copy
novo.add(4)
print(s)
print(novo)

novo = s # Shallow copy
novo.add(4)
print(s)
print(novo)

# clear
s.clear()
print(s)

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

# union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# difference
so_paython = estudantes_python.difference(estudantes_java)
print(so_paython)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

s = {1,2,3,4,5,6}
# sum
print(sum(s))
# max
print(max(s))
# min
print(min(s))
# len
print(len(s))




