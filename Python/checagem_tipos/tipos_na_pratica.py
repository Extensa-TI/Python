"""
nomes: list = ['Geek', 'University']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)

from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Geek', 'University']
versoes: Tuple[int, int, int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'bancos_couro': True}
valores: set[int] = {3, 4, 5, 6, 7}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""
import random
from typing import  List, Tuple, Set, Dict

NAIPES = '♤ ♡ ♧ ♢'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]

def criar_barralho(aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho: BARALHO = [(n,c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO,BARALHO,BARALHO,BARALHO]:
    """Gerencia a mão de cartas"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar() -> None:
    """Inicia um jogo"""
    cartas: BARALHO = criar_barralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}
 
    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j,c) in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()

#print(NAIPES)
#print(CARTAS)

#print(criar_barralho())

#baralho = criar_barralho()
#print(distribuir_cartas(baralho))

