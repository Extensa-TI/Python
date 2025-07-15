"""
assert-> retorna None se for verdadeira e AssertionError se for falsa

ALERTA-> SE UM PROGRAMA PYTHON FOR EXECUTADO COM O PARÂMETRO -O (o maiúsculo), NENHUM ASSERTIONS
SERÁ VALIDADO.

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2,4)
print(ret)
ret = soma_numeros_positivos(-2,4)
print(ret)
"""

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comento {comida}'

comida = 'batata frita'
print(comer_fast_food(comida))

