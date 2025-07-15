"""
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)
print(media)

res = filter(lambda x: x > media,dados)
print(list(res))
print('Usando novamente o resultado, a res sera vazia')
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res = filter(None,paises)
print(list(res))

usuarios = [
    {'username' : 'samuel', 'tweets' : ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username' : 'carla', 'tweets' : ['Eu amo meu gato']},
    {'username' : 'jeff', 'tweets' : []},
    {'username' : 'bob123', 'tweets' : []},
    {'username' : 'doggo', 'tweets' : ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username' : 'gal', 'tweets' : []}
]

#print(usuarios)

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

"""
nomes = ['Vanessa','Ana', 'Maria']
lista = list(map(lambda nome: f'Sua intrutora e {nome}', filter(lambda x: len(x) < 5,nomes)))
print(lista)
