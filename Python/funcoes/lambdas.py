"""
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

nome_completo = lambda nome,sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('angelina', 'joile'))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Henlein','Arthur C Clarke','Frank Hebert','Orson Scott Card', 'Douglas Adam', 'H. G. Wells', 'Leigh Bracket']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""
# Funcao quadratica
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2,3,-5)
print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(2,3,-5)(2))


