"""
lista = [1,8,4, 99, 34,129]
print(max(lista))

tupla = (1,8,4, 99, 34,129)
print(max(tupla))

conjunto = {1,8,4, 99, 34,129}
print(max(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario))
print(max(dicionario.values()))

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
print(max(val1, val2))

lista = [1,8,4, 99, 34,129]
print(min(lista))

tupla = (1,8,4, 99, 34,129)
print(min(tupla))

conjunto = {1,8,4, 99, 34,129}
print(min(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(min(dicionario))
print(min(dicionario.values()))

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
print(min(val1, val2))

nomes = ['Arya','Samson','Dora','Tim','Ollivander']
print(max(nomes))
print(min(nomes))
print(max(nomes,key=lambda nome: len(nome)))
print(min(nomes,key=lambda nome: len(nome)))

"""
musicas = [ {'titulo':'Thunderstruck','tocou':3},
            {'titulo':'Dead Skin Mask','tocou':2},
            {'titulo':'Back in Black','tocou':4},
            {'titulo':'Too old to rock in roll, too young to die','tocou':32} 
          ]

print(max(musicas, key= lambda musica: musica['tocou']))
print(min(musicas, key= lambda musica: musica['tocou']))
print()
print(max(musicas, key= lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key= lambda musica: musica['tocou'])['titulo'])
