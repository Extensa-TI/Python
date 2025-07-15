print("""
A funcao all() retorna true se todos os elementos do iteravel 
for true ou se o iteravel esta vazio""")

"""
print(all([0,1,2,3,4]))

nomes = ['Carlos', 'Cintia', 'Carla', 'Casiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))

"""
print("""
A funcao any() retorna true se qualquer elementos do iteravel 
for true. Se o iteravel esta vazio retorna false""")

print(any([0,1,2,3,4]))
print(any([0,False,{},[],()]))

nomes = ['Carlos', 'Cintia', 'Carla', 'Casiano', 'Cristina','Vanessa']
print(any([nome[0] == 'V' for nome in nomes]))
print(any([num for num in [4,2,10,6,8,9] if num %2 == 0]))


