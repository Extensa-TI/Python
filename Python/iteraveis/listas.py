lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', '', 'U','n', 'i','v','e','r','s','i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# in
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# sort
lista1.sort()
print(lista1)

# count
print(lista1.count(1))
print(lista5.count('e'))

# append
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8,3,1])
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei a lista.')
else:
    print('Não encontrei a lista.')

# extend
lista1.extend([127,44,67])
print(lista1)

# insert
lista1.insert(2,'Novo valor')
print(lista1)

# concatenar
lista6 = lista1 + lista2
print(lista6)

# concatenar com extend
lista7 = lista1
print(lista7)
lista7.extend(lista2)
print(lista7)

# reverse
print(lista2)
lista2.reverse()
print(lista2)
print(lista2[::-1])

# copy
lista8 = lista2.copy()
print(lista8)

print(len(lista1))

# pop - deleta e retornar o último elemento
print(lista1)
deletado = lista1.pop()
print(lista1)
print(deletado)
lista1.pop(2) # remove pelo índice
print(lista1)

# clear - limpa a lista
print(lista1)
lista1.clear()
print(lista1)

# multiplicando a lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# split
curso = 'Programação Python: essencial'
print(curso)
print(curso.split()) 
print(curso)

curso = 'Programação, Python,essencial'
print(curso)
curso = curso.split(',')
print(curso)

#join
curso = ' '.join(curso)
print(curso)

# acessando por índice
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])

#enumerate
for indice, cor in enumerate(cores):
    print(f'{indice} {cor}')

#index  Quando não encontra gera o valueError
lista = [5, 6, 7, 5, 8, 9, 10]
print(lista.index(6))
print(lista.index(5)) # pega o primeiro
print(lista.index(5,1)) # pega a partir do índice 1
print(lista.index(8, 2,6))

# slicing
lista = [1, 2, 3, 4]
print(lista[::])  # sem parâmetro
print(lista[1:])  # só início
print(lista[-1:]) # só inicio
print(lista[:2])  # só fim -1 O valor de fim não é inclusivo
print(lista[1:3]) # inicio e fim
print(lista[::2]) # só o passo
print(lista[::-1]) # inverte a lista

# soma sum()
lista = [1,2,3,4,5,6]
print(sum(lista))

# max()
print(max(lista))

# min()
print(min(lista))

# len()
print(len(lista))

# transformando lista em tupla
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desempacotamento de lista
lista = [1,2,3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# copiando uma lista (Shallow copy e Deep copy)
# Deep copy
nova_lista = lista.copy() 
print(nova_lista)
nova_lista.append(4)
print(nova_lista)
print(lista)

# Shallow copy
print(lista)
nova_lista = lista
nova_lista.append(4)
print(lista)
print(nova_lista)
