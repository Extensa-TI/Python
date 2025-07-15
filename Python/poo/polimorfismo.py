"""
"""

class Animal:

    def __init__(self,nome):
        self.__nome = nome
    
    def falar(self):
        raise NotImplementedError('A classe filha precisar implementar esse método')
    
    def comer(self):
        return f'{self._Animal__nome} está comendo....'

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return f'{self._Animal__nome} fala au au'

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return f'{self._Animal__nome} fala miau'

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return f'{self._Animal__nome} fala crick'

felix = Gato('Felix')
print(felix.comer())
print(felix.falar())

pluto = Cachorro('Pluto')
print(pluto.comer())
print(pluto.falar())

mickey = Rato('Mickey')
print(mickey.comer())
print(mickey.falar())

