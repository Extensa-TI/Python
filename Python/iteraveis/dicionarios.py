print(type({}))

paises = {'br':'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

paises = dict(br='Brasil', eua='Estados Unidos', py= 'Paraguai')
print(paises)

# acessando os dicionários
print(paises['br'])

# get
print(paises.get('br')) # recomendado
print(paises.get('ru'))

# valor padrão
pais = paises.get('ru', 'Não encontrado')
print(pais)

# in
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Qualquer tipo de dado pode ser chave
localidades = {
    (35.6895, 396917) : 'Escritório em Tóquio',
    (40.7127, 740060) : 'Escritório em Nova York',
    (37.7749, 1224194) : 'Escritório em São Paulo'
}

# adicionando elementos
receita = {'jan':100, 'fev':120, 'mar':300}
receita['abr'] = 350
print(receita)

novo_dado = {'mai':500}
receita.update(novo_dado)
print(receita)

receita.update({'jun':550})
print(receita)

# atualizando dados
receita['mai'] = 600
receita.update({'abr':200})
print(receita)

# removendo dados
receita.pop('jun')
print(receita)
ret = receita.pop('mai')
print(ret)
print(receita)

del receita['abr']
print(receita)

# utilização dos dicionários
# Exemplo: carrinho de compras

# 1 - Usando lista - Teriamos que saber o indice de cada item do produto
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of war 4',1,150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# 2 - Usando tupla - Teriamos que saber o indice de cada item do produto
carrinho = ()
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of war 4',1,150.00)
carrinho = (produto1,produto2)
print(carrinho)

# 3 - Usando dicionário
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Good of war 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# clear()

d = dict(a = 1, b = 2, c = 3)
print(d)
d.clear()
print(d)

# copiando um dicionário
novo = d.copy()    # deep copy
print(novo)
novo['a'] = 1
print(novo)
print(d)

outro = d   # shallow copy
print(outro)
outro['b'] = 2
print(outro)
print(d)

# forma não usual de criar um dicionario

dc = {}.fromkeys('a',1)
print(dc)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,10),'novo')
print(veja)

receita = {"jan": 100, "fev": 250, "mar":400}
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# keys()
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# values()
print(receita.values())

for valor in receita.values():
    print(valor)

# items()
print(receita.items())
for chave, valor in receita.items():
    print(f'{chave} : {valor}')

# sum()
print(sum(receita.values()))

# max()
print(max(receita.values()))

# min()
print(min(receita.values()))

# len()
print(len(receita))

