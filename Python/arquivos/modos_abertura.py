"""
r-> Modo de leitura (padrao)
w-> Modo de escrita
x-> Abre para escrita somente se o arquivo nao existir
a-> Abre para escrita e adiciona no final arquivo, se o arquivo nao existir e criado
+-> Abre para o modo de atualizacao, leitura e escrita

try:
    with open('recursos/texto.txt','x') as arquivo:
        arquivo.write("Teste de conteudo")
except:
    print('Arquivo já exite')

"""
with open('recursos/texto.txt', 'a') as arquivo:
    
    while True:
        fruta = input('Informe um fruta ou digite sair: ')
        if fruta != 'sair': 
            arquivo.write(fruta + '\n')
        else: break
