"""
Em Python, dividimos os métodos em dois grupos
- Métodos de instância
- Métodos de classe

São escritos em letras minúsculas e se o nome for composto serparado por underline
"""

# Método de instância

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador
        self.__limite = limite
        self.__saldo = saldo
        self.__ligado = False
        self.__numero = self.__numero + 1
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    @classmethod
    def conta_produtos(cls):
        print(f'Temos {cls.contador} produto(s) no sistema')
    
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self,nome, descricao, saldo):
        self.__id = Produto.contador
        self.__nome = nome
        self.__descricao = descricao
        self.__saldo = saldo
        self.__id = self.__id + 1
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__saldo * (100-porcentagem))/100

from passlib.hash import pbkdf2_sha256 as crypto
class Usuario:

    def __init__(self, nome, sobrenome,email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypto.hash(senha)
        print(f'Usuário criado: {self.__gera_usuario()}')
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if crypto.verify(senha, self.__senha):
            return True
        return False

    # método privado    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

p1 = Produto('Playstation 4', 'video game', 2300)
print(p1.desconto(50))
print()

user1 = Usuario('Angelina', 'Joile', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')
print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user2))
print()

print(f'Senha User 1: {user1._Usuario__senha}')
print(f'Senha User 2: {user2._Usuario__senha}')
print()

#nome = input('Informe o nome: ')
#sobrenome = input('Informe o sobrenome: ')
#email = input('Informe o email: ')
#senha = input('Informe a senha: ')
#confirma_senha = input('Confirme a senha: ')

#if senha == confirma_senha:
#    user = Usuario(nome,sobrenome,email,senha)
#else:
#    print('Senha não confere...')
#    exit(1)

#print('Usuário criado com sucesso!')

#senha = input('Informa a senha para acess: ')

#if user.checa_senha(senha):
#    print('Acesso permitido')
#else:
#    print('Acesso negado')
#print()


p1 = Produto('Playstation 4', 'video game', 1300.00)
# Métodos de classe -> é necessário decorar com @classemethod. O parâmetro cls é de classe
Produto.conta_produtos()

# Métodos estáticos -> é necessário decorar com @staticmethod.
print(Produto.definicao())
print()

u1 = Usuario('Carol', 'Green', 'carol@gmail.com', '1234')




