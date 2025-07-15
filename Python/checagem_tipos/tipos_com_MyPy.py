"""
usar o mypy para checar os tipos

no console: mypy tipos_com_MyPy.py
"""

def cabecalho(texto: str, alinhamento: bool = True)-> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')

print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))
