"""
Exemplo: Acessando elementos privados fora da classe (Name Mangling)

_classe_elemento
_instancia_Pessoa_nome
_instancia_Pessoa_falar()

Abstração-> é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados.
"""

class ContaCorrente:

    contador = 399

    def __init__(self, titular, saldo, limite):
        self.numero = ContaCorrente.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.numero += 1
        ContaCorrente.contador = self.numero
    
    def extrato(self):
        return f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}'
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self,valor):
        self.saldo -= valor