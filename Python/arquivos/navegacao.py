"""
# diretorio corrente absoluto
print(os.getcwd())

# voltar um diretorio
os.chdir('..')
print(os.getcwd())

# checar se um diretorio e relativo ou absoluto
print(os.path.isabs('c:/Users'))
print(os.path.isabs('Users'))

import sys

# podemos identificar o sistema operacional (nt = windows)
print(os.name)

# para mais informações sobre o so
print(sys.platform)

# exemplo de mudar diretorio
print(os.getcwd())
re = os.path.join(os.getcwd(),'Arquivos')
# re = os.path.join(os.getcwd(),'Arquivos','outro diretorio','outro diretorio)
os.chdir(re)
print(os.getcwd())

# listar arquivos e diretorios
print(os.listdir())
print(os.listdir('c://'))

"""
import os

# listar arquivos e diretorios com mais detalhes
scanner = os.scandir();
arquivos = list(scanner)
print(arquivos)
print(arquivos[0].name)
# E preciso fechar o arquivo.
scanner.close()





