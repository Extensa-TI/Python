"""
"""

def diz_oi():
    """Uma funcao simples que retorna a string Oi!"""
    return 'Oi!'

print(help(diz_oi))

print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de um numero
    ou numero a potencia
    :param numero: numero que desejamos gerar o exponencial
    :param potencia:potencia do numero, por padrao e 2
    :return: retorna a potencia do numero
    """
    return numero ** potencia

print(help(exponencial))
