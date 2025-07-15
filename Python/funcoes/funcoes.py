"""
from random import random

cores = ['verde','amarelo','azul','branco']
print(cores)

def diz_oi():
    print('Oi!')

diz_oi()

def cantar_parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida.')
    print('Viva o aniversariante!')

canta = cantar_parabens

canta()

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print(f'Retorno {ret}')
print(f'Retorno {quadrado_de_7()}')

def funcao_retornando_varios():
    return 1, 2, 3, 4, 5

nun1, nun2, nun3, nun4, nun5 = funcao_retornando_varios()

print(f'{nun1} {nun2} {nun3} {nun4} {nun5}')
print(funcao_retornando_varios())

def joga_moeda():
    # gera um valor pseudo-randomica de 0 a 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida.')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Marcos')

def outra(num1,b,msg):
    return (num1 + b) * msg

print(outra(2,3,'Geek '))

# nomeando parametros
def nome_completo(nome, sobrenome):
    return f'Seu nome e {nome} {sobrenome}'

print(nome_completo('Angelina', 'Joile'))
# parametros sao variaveis passadas na definicao da funcao
# argumentos sao dados passados durante a execucao da funcao
# a ordem dos parametros importam

# argumentos nomeados (keyword arguments)
print(nome_completo(sobrenome='Joile', nome='Angelina'))

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7]

print(soma_impares(lista))

# funcoes com paramentros padrao

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2,3))
print(exponencial(3))

# em funcoes com parametro default sempre deve estar no final

def soma(num1,num2):
    return num1 + num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2,subtracao))

instrutor = 'Geek'

def diz_oi():
    instrutor = 'Pyhton'
    return f'Ola {instrutor}'

print(diz_oi()) # Ola Python
print(instrutor) # Geek

total = 0

def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
print(total)

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total
