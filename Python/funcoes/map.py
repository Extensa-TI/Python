"""
Mapeamento de valores para funcao

import math

def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2,5,7.1,0.3,10,44]

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

areas = map(area,raios)
print(type(areas))
print(list(areas))
print('Depois da primeira utilizacao do map ele retorna uma lista vazia')
print(list(areas))

print(list(map(lambda r: math.pi * (r ** 2),raios)))

"""
cidades = [('Berlin', 29),('Cairo',36),('Buenos Aires',19),('Los Angeles',26),('Tokio',27),('Nova Yoork',28),('Londres',22)]

c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)
print(list(map(c_para_f,cidades)))
