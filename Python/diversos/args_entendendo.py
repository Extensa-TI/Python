"""
def soma_todos_numeros(*args):
        return sum(args)

print(soma_todos_numeros(1,2,3,4,5))

def soma_todos_numeros(nome, sobrenome,*args):
        return f'{nome} {sobrenome} {sum(args)}'

print(soma_todos_numeros('Angeline', 'Joile',1,2,3,4,5))
"""

def soma_todos_os_numeros(*args):
    return sum(args)

print(soma_todos_os_numeros(1,2,3,4,5))

numeros = [1,2,3,4,5]

n1, n2, n3, n4, n5 = numeros

print(soma_todos_os_numeros(n1,n2,n3,n4,n5))

print(soma_todos_os_numeros(*numeros)) # mais pratico - passa uma coleçao que sera desempacotada
