"""
Decorators com diferentes assinaturas

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Ola, eu sou o/a {nome}"

@gritar
def ordenar(principal,acompanhamento):
    return f"O prato principal é {principal} é o acompanhamento e {acompanhamento}"

print(saudacao("Pedro"))

print(ordenar("Picanha","Batata Frita"))


"""
# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args

@verifica_primeiro_argumento(10)
def soma_dez(num1,num2):
    return num1 + num2;

print(soma_dez(10,12))
print(soma_dez(1,21))
print(comida_favorita('pizza','churrasco'))
print(comida_favorita('sanduiche', 'pizza'))



