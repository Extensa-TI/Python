"""

""" 

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        self.__ligada = not self.__ligada

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador
        self.__limite = limite
        self.__saldo = saldo
        self.__ligado = False
        self.__numero = self.__numero + 1
        ContaCorrente.contador = self.__numero

class Usuario:

    def __init__(self, nome, sobrenome,email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

lamp1 = Lampada('branca', 110, 60)
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')


cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

