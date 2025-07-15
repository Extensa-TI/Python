"""
seek()-> utilizada para movimentar o cursor pelo arquivo
readLine()-> le o arquivo linha a linha
readLines()-> coloca cada linha numa lista
close()-> fechar o arquivo no final
closed*()-> verifica se o arquivo está aberto

"""
arquivo = open('recursos/texto.txt')
print(arquivo.read())
print('------------------')

arquivo.seek(0)
print(arquivo.read())
print('------------------')

arquivo.seek(29)
print(arquivo.read())
print('------------------')

arquivo.seek(0)
print(arquivo.readline())
print('------------------')

arquivo.seek(0)
print(arquivo.readlines())
print('------------------')

arquivo.seek(0)
print(arquivo.read(50))
print('------------------')

print(arquivo.closed)
arquivo.close()
