from models.cliente import Cliente
from utils.helper import format_float_str_moeda

class Conta:
    codigo: int = 1001

    def __init__(self, cliente: Cliente):
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self,valor: float):
        self.__saldo = valor

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, valor: float):
        self.__limite = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @property
    def _calcula_saldo_total(self) -> float:
        return self.__saldo + self.__limite

    def depositar(self, valor: float):
        pass

    def sacar(self, valor: float):
        pass

    def transferir(self, destino: object, valor: float):
        pass

    def __str__(self) ->str:
        return f'Numero da conta: {self.numero}\nCliente: {self.cliente.nome}\nSaldo Total: {format_float_str_moeda(self.saldo_total)}'
