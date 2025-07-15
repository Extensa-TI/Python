"""
import json

ret = json.dumps(['produto',{'Playstion 4':('2TB','Novo','220V',2340)}])
print(type(ret))
print(ret)

import json

class Gato:

    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
felix = Gato('Felix', 'Angora')
ret = json.dumps(felix.__dict__)
print(felix.__dict__)
print(ret)

import jsonpickle

class Gato:

    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
felix = Gato('Felix', 'Angora')
ret = jsonpickle.encode(felix)
print(ret)

# Escrevendo o arquivo
class Gato:

    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
felix = Gato('Felix', 'Angora')

with open('recursos/felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)  

"""
import jsonpickle

# Lendo o arquivo
class Gato:

    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
with open('recursos/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
