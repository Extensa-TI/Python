valor = '67.3'
print(float(valor))

def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome = 'Geek'))

def cumprimenta_v2(nome, /):
    return f'Olá {nome}'

print(cumprimenta_v2('Geek'))
#print(cumprimenta_v2(nome = 'Geek')) erro: o argumento nome é somente posicional

def cumprimenta_v3(nome, /, mensagem = 'Olá'): # O que está antes da barra é posicional
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('Felicity', mensagem= 'Bem-vinda'))
print(cumprimenta_v3('University', 'Hello'))

def cumprimenta_v4(nome, mensagem = 'Olá', /):
    return f'{mensagem} {nome}'

print(cumprimenta_v4('Geek', 'Hello'))
#print(cumprimentar_v4('Geek', mensagem = 'Hello')) # erro: todos os argumentos são posicionais

def cumprimenta_v5(*, nome):
    return f'Olá {nome}'

#print(cumprimenta_v5('Geek')) erro: obrigatório passar o argumento de todos após o *, conforme abaixo
print(cumprimenta_v5(nome='Geek'))

def cumprimenta_v6(nome, /, mensagem1 = 'Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimenta_v6('Geek', 'Hello', mensagem2='tenha um bom dia'))
