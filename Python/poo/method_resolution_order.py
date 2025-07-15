"""
Em Python pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
- Via propriedade da classe __mro__
- Via método mro()
- Via help

"""
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
    
class Pinguim(Aquatico,Terrestre):
    
    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('Tux')

#class Pinguim(Terrestre,Aquatico): Eu sou Tux da terra.- Method Resolution Order - MRO

#class Pinguim(Aquatico,Terrestre): Eu sou Tux do mar.- Method Resolution Order - MRO
print(tux.cumprimentar()) 

print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))