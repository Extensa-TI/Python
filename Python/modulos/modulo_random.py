"""
Modulo Random -> Possui varias funções para gerar numeros pseudo-aleatorios

Existem duas formas de se utilizar um modulo ou funcao:
- Importando todo o modulo (nao recomendado)
- Importando uma funcao especifica do modulo

randon() -> Gera um numero real pseudo-aleatorio entre 0 e 1

import random
print(random.random())

from random import random
print(random())

for i in range(10):
    print(random())

uniform()-> Gerar um numero real pseudo aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3,7))

from random import randint

for i in range(6):
    print(randint(1,61), end=', ')

choice()-> Mostra um valor aleatorio entre um iteravel

from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']

print(choice(jogadas))
print(choice('Geek Universy'))

shuffle()-> Embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A','2','3']
shuffle(cartas)
print(cartas)
"""
