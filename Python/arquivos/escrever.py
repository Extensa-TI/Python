"""
Ao abrir um arquivo para escrita, o arquivo, se nao existir, e criado um arquivo

with open('diversos/texto.txt', 'w') as arquivo:
    arquivo.write('Escrever dados num arquivo e muito facil\n')
    arquivo.write('Podemos colocar quantas linha quisermos\n')
    arquivo.write('Esta e a ultima linha\n')

with open('recursos/texto.txt', 'w') as arquivo:
    arquivo.write('Geek' * 1000)

"""
with open('recursos/texto.txt', 'w') as arquivo:
    
    while True:
        fruta = input('Informe um fruta ou digite sair: ')
        if fruta != 'sair': 
            arquivo.write(fruta + '\n')
        else: break
