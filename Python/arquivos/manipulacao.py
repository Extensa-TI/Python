"""
# descobrindo se um arquivo ou diretorio existe
print(os.path.exists('recursos/texto.txt'))

# criando arquivos
open('recursos/teste.txt','w').close()

# criando diretorios
os.mkdir('recursos/diretorio')

# criando v�rios diretorios
os.makedirs("templates/geek/university")
# se j� existir n�o dar erro
os.makedirs("templates/geek/university", exist_ok=True)

# renomear arquivos e diretorios
# se o diretorio nao estiver vazio = OSerror
os.rename('template2', 'geek2')

# deletar arquivos (CUIDADO) nao vai para a lixeira
os.remove('geek.txt')

# remover diretorios - se n�o estiver vazio teremos um OSError
os.rmdir('templates')

# removendo uma arvore de diretorios vazios
os.removedirs('geek2/mais')

import os
import tempfile

# usando aquivos temporarios (so existe enquanto usado)
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp,'arquivo_temporario.txt'),'w') as arquivo:
        arquivo.write('Geek University\n')

# criando arquivo temporario -> b para arquivo binario
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University')
print(arquivo.name)
input()
arquivo.close()

"""

