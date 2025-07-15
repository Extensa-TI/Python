"""
Todos os métodos que utilizam dunder

__repr__ -> igual ao toString()

__str__ -> toString()
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
    
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'
    

livro1 = Livro('Python Rocks', 'Geek Universitu', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)





