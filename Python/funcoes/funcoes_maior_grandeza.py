"""
Higher Order Funcions (Funcoes de Maior Grandeza)
- Funcoes que recebem outras funcoes como parametro
- Funcoes que retornam outras funcoes
- Funcoes que recebem e retornam outras funcoes

def somar(a, b):
    return a + b    

def subtract(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 5, somar))
print(calcular(4, 5, subtract))
print(calcular(4, 5, multiplicar))
print(calcular(4, 5, dividir))

# Funcoes aninhadas (nested functions)
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce ')) 
    return humor() + pessoa

print(cumprimento('Ana'))
print(cumprimento('Pedro'))
print(cumprimento('Maria'))

# Exemplo de funcao que retorna outra funcao
from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkkkkkk', 'yayayayayayay'))
    return rir  

rindo = faz_me_rir()
print(rindo())
print(rindo())

"""

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahah ', 'kkkkkkkkkkkk ', 'yayayayayayay '))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Fernando')
print(rindo())






