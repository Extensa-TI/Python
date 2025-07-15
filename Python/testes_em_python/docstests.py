"""
Doctests sao testes na docstring
"""
def soma(a,b):
    """soma os numeros a e b
    
    >>> soma(1,2)
    3
    >>> soma(6,4)
    10
    """
    return a + b

print(soma(3,4))

# teste no console python -m doctest -v doctests.py

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1,2,3,4])
    [2,4,6,8]
    >>> duplicar([])
    []
    >>> duplicar(['a','b','c'])
    ['aa','bb','cc']
    >>> duplicar([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    #pass
    #return [] # passou um no teste
    return [2 * elemento for elemento in valores] # todos passaram no teste

# erro inexperado
def fala_oi():
    """fala oi
    
    >>> fala_oi()
    "oi"
    """
    return "oi"   # teste falha porque retorna oi com aspas simples


def verdade():
    """ Retorna verdade
    
    >>> verdade()
    True               # Em algumas plataformas, quando da espaços depois do True o teste falha
    """
    return True

