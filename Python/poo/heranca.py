"""
"""

class Pessoa:

    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self._cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Client(Pessoa):

    def __init__(self,nome, sobrenome, cpf,renda):
        Pessoa.__init__(self,nome, sobrenome, cpf) # forma não comum de acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome,sobrenome,cpf) # forma comum de acessar a super classe
        self.__matricula = matricula

cliente1 = Client('Angelina', 'Joile', '123.456.789-00',5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
