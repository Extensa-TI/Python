"""
Annotations ->  texto: str (str é um annotations)
def cabecalho(texto: str, alinhamento: bool = True)-> str:  bool e -> str são annotations

"""

import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = "Geek University"
peso: float = 67.9
print(__annotations__)

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'

p = Pessoa(nome = "Geek University", idade=37, peso=59.5)
print(p.__dict__)

#print(p.__annotations__) não tem annotations

print(p.andar.__annotations__)
print(p.__init__.__annotations__)
