"""
Atributos-> Representam as características do objeto.

Em Python, dividimos os atributos em 3 grupos:
- Atributos de Instância
- Atributos de Classe
- Atibutos Dinâmicos
"""

# Atributos de Instância -> São atributos declarados dentro do método construtor
# Atributos podem ser Públicos ou Privados
# Por convenção, ficou estabelecido que, todo atribuito de uma classe é público

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Para ser privado utiliza-se __ duplo undescore no inicio do seu nome (Name Mangling)

class Acesso:

    def __init__(self, email, senha):
        self.email = email # público
        self.__senha = senha # privado

    def mostra_senha(self):
        return self.__senha

# Lembre-se que isso é apenas uma convenção, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe

user = Acesso('user@gmail.com', 1234)

print(user.email)
# print(user.__senha) # erro de execução: AttributeError

print(user._Acesso__senha) # temos acesso, mas não deveriámos fazer este acesso (Name Mangling)

print(user.mostra_senha())

# Atributos de classe-> Atributos declarados diretamente na classe, ou seja, fora do contrautor
# geralmente iniciamos um valor que é compartilhado por todas as instâncias da classe

class Produto:

    imposto = 1.05 # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto 
        Produto.contador = id
    
p1 = Produto('PlayStation 4', 'video game', 2300)
p2 = Produto('Xbox 5', 'video game', 4500)

print(p1.imposto)
print(p2.imposto)
print(p1.valor)
print(p2.valor)
print()

# Não precisamos criar uma instância para ter acesso aos atributos de classe
print(Produto.imposto)
print()

# Atributos Dinâmicos-> pode ser criado em tempo de execução e será exclusivo da instância que o criou (não é comum)

p1 = Produto('PlayStation 4', 'vídeo game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Peso: {p2.peso}, Valor: {p2.valor}')
print()

# Deletando atributos dinamicamente
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
print(p2.__dict__)
del p2.valor
print(p2.__dict__)
print()



