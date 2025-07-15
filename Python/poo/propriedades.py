"""
class Conta:
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__numero = Conta.contador + 1
        Conta.contador = self.__numero
    
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self,valor):
        self__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite
    
    
c1 = Conta('Felicity', 3000, 5000)
c2 = Conta('Angelina', 2000, 4000)

print(c1.extrato())
print(c2.extrato())

soma = c1.get_saldo() + c2.get_saldo()
print(soma)

print(c1.get_limite())
c1.set_limite(99999)
print(c1.get_limite())

"""

class Conta:
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__numero = Conta.contador + 1
        Conta.contador = self.__numero
    
    @property 
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Em python é possivel ter métodos como propriedades
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self,valor):
        self__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
c1 = Conta('Felicity', 3000, 5000)
c2 = Conta('Angelina', 2000, 4000)

print(c1.extrato())
print(c2.extrato())

soma = c1.saldo + c2.saldo
print(f'A soma do saldo das contas é {soma}')

print(f'Limite de {c1.titular} {c1.limite}')
c1.limite = 7543
print(f'Limite de {c1.titular} {c1.limite}')

print(f'Valor total = {c1.valor_total}')


