"""
A herança multípla pode ser feita de dias maneiras:
- Por multiderivação direta
- Por multiderivação indireta
"""

# Multiderivação direta

class Base1:
    pass

class Base2:
    pass

class MultiDerivadaDireta(Base1,Base2):
    pass

# Multiderivação indireta

class Classe1:
    pass

class Classe2(Classe1):
    pass

class MultiDerivadaIndereta(Classe1):
    pass

class Animal:

    def __init__(self,nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'
    
class Terrestre(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def andar(self):
        return f'Eu {self._Animal__nome} estou andando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra.'
    
class Pinguim(Terrestre,Aquatico):
    
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # Eu sou Tux da terra.- Method Resolution Order - MRO

print(f'Tux é instância de Pinguin? {isinstance(tux,Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux,Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux,Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux,Animal)}')
print(f'Tux é instância de Object? {isinstance(tux,object)}')


