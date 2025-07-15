"""
Pickle -> realiza o seguinte processo:
Objetos Python -> Binarização
Binarização -> Objetos Python
Esse processo é chamado de serializaçao/deserialização

Obs: O módulo Pickle não é seguro contra dados maliciossos e desta forma
não é recomendado trabalhar com arquivos pickle vindo de outras pessoas
que não conheça ou de fontes desconhecidas.

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('recursos/animais.pickle', 'wb') as arquivo:
    pickle.dump((felix,pluto), arquivo)

"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def comer(self):
        print(f'{self.__nome} está comendo....')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def mia(self):
        print(f'{self._Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def late(self):
        print(f'{self._Animal__nome} está latindo...')

with open('recursos/animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    print(f'O cachorro chama-se {cachorro._Animal__nome}')
    gato.mia()
    cachorro.late()

