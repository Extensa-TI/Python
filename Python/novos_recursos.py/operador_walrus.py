"""
Permite fazer a atribuição e retorno de valor em uma única expressão

variavel := expressao
"""
nome = 'Geek University'
print(nome)

print(nome := 'Geek University')

cesta = []
#fruta = input('Informe a fruta: ')
#while fruta != 'jaca':
#    cesta.append(fruta)
#    fruta = input('Informe a fruta: ')

while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
