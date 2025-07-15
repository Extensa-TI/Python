"""
Entendendo Iterators e Iteraveis

Itarator-> 
    - Um objeto que pode ser Iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() e chamada

Iteravel->
    - Um objeto que ira retornar um Iterator quando a funcao iter() for chamada

nome = 'Geek' # E um itarable 
numeros = [1,2,3,4,5,6] # E um itarable

# print(next(nome)) # Erro objeto nao e um iterator
it1 = iter(nome)
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

"""



