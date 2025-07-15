"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} e {cor.title()}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek" 
    return 'Nao tenho certeza quem voce e...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Nas funcoes podemos ter (NESTA ORDEM)

- Parametros obrigatorios
- *args
- Parametros defult
- **kwargs

def minha_funcao(idade,nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if (solteiro):
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8,'Julia')
minha_funcao(18, 'Felicity', 4,5,3,solteiro=True)
minha_funcao(34, 'Felipe', eu='Nao',voce='Vai')
minha_funcao(19,'Carla',9,4,3,java=False, python=True)

# funcao com a ordem correta de parametros
def mostra_info(a,b,*args,instrutor='Geek',**kwargs):
    return [a,b,args,instrutor,kwargs]

print(mostra_info(1,2,3,sobrenome='University',cargo='Instrutor'))

# funcao com a ordem errada de parametros
def mostra_info(a,b,instrutor='Geek',*args,**kwargs):
    return [a,b,args,instrutor,kwargs]

print(mostra_info(1,2,3,sobrenome='University',cargo='Instrutor'))

# desempacotar kwargs
def mostra_nomes(**kwargs):
    return kwargs

nomes = {'nome' : 'Felicity', 'sobrenome' : 'Jones'}

print(mostra_nomes(nome='Felicity',sobrenome='Jones'))
print(mostra_nomes(**nomes))

"""
def soma_numeros(a,b,c):
    print(a+b+c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = dict(a=1,b=2,c=3)

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)
soma_numeros(**dicionario) # os nomes das chaves do dicionario deve ser igual ao nome dos parametros
