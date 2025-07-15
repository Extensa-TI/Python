"""
Usando o mypy ele acusa o type hinting
"""
import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8))

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

def cabecalho2(
    texto,  # type: str
    alinhamento=True  # type bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

nome = "Geek University"  # type: str
