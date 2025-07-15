"""
print("Retorna uma lista de um iteravel")
numeros = (6,1,8,2)
print(sorted(numeros))
print(numeros)
print()

print(sorted(numeros,reverse=True))
print(set(sorted(numeros)))
print()

usuarios = [
    {'username' : 'samuel', 'tweets' : ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username' : 'carla', 'tweets' : ['Eu amo meu gato']},
    {'username' : 'jeff', 'tweets' : []},
    {'username' : 'bob123', 'tweets' : []},
    {'username' : 'doggo', 'tweets' : ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username' : 'gal', 'tweets' : []}
]
print(sorted(usuarios,key=lambda usuario:usuario['username']))
print()
print(sorted(usuarios,key=lambda usuario:len(usuario['tweets'])))
print()

"""
musicas = [ {'titulo':'Thunderstruck','tocou':3},
            {'titulo':'Dead Skin Mask','tocou':2},
            {'titulo':'Back in Black','tocou':4},
            {'titulo':'Too old to rock in roll, too young to die','tocou':32} 
          ]
print(sorted(musicas,key=lambda musica:musica['tocou']))
