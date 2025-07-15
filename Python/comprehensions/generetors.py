from sys import getsizeof

nomes = ['Carlos','Camila','Carla','Cassiano','Cristina','Vanessa']
print(any([nome[0] == 'C' for nome in nomes])) # list comprehension
print(any(nome[0] == 'C' for nome in nomes)) # generator

res = [nome[0] == 'C' for nome in nomes]
print(type(res))

res = (nome[0] == 'C' for nome in nomes)
print(type(res))

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(set_comp)
print(dic_comp)
print(gen)

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)
