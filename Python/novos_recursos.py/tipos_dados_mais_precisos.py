"""
Tipos mais precisos
-> Literal Type
-> Union
-> Final
-> Typed dictionares
-> Protocols

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro('Geek'))

from typing import Literal

# Literal
def pegar_status(usario: str) -> Literal['conectado', 'desconectado']:
    pass

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}') # !r coloca a operação entre aspas simples
    
calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
#calcula_v1('*',3, 5) exceção ValueError: Operação inválida '*'

def calcula_v2(operacao: Literal['+','-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}') # !r coloca a operação entre aspas simples
    
calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
#calcula_v2('*',3, 5) # exceção ValueError: Operação inválida '*' no mypy pega o erro

#Union
from typing import Union

def soma(num1: int, num2: int) -> Union[str,int]:
    resultado = num1 + num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado

print(soma(1, 3))
print(soma(26, 31))

# Final
from typing import Final

NOME: Final = 'Geek'

print(NOME)

NOME: Final = 'University' 

print(NOME) # o mypy acusa o erro de já ter uma variavel Final

# final
from typing import final

@final
class Pessoa:
    pass

class Estudante(Pessoa): # não poderia porque Pessoa é final
    pass

    @final
    def estudar(self):
        print(f'Estou estudando')

class Estagiario(Estudante):
    pass

    def estudar(self): # não poderia sobrescrever o método porque é final na super classe
        print('Estou estagiando')

# o mypy pega esses erros

# Typed Dicitionares
from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)
outro = CursoPython(algo='vai', coisa=True)
print(outro) # o mypy pega esse erro
"""
# Protocols
from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudado o curso {valor.titulo}')

class Venda:
    pass

class Venda2:
    titulo = 'oi'

v1 = Venda()

#estudar(v1) # erro porque venda não tem o atributo titulo

v2 = Venda2()

print(v2.titulo)




