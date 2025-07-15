nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1,10): # O valor final não é inclusivo
    print(numero)

for i, v in enumerate(nome):
    print(i)

for i,_ in enumerate(nome): # Quando não precisamos de um valor podemos descartá-lo usando o underline
    print(i)

for _,v in enumerate(nome): # Quando não precisamos de um valor podemos descartá-lo usando o underline
    print(v)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

for letra in nome:      # imprimir na mesma linha
    print(letra,end='')

for num in range(1,11):
    print('\U0001F60D' * num)

    