"""
__main__
__name__

Em python são utilizadas dunder para criar funções, atributos, propriedades e etc
utilizando double under para não gerar conflitos desses elementos na programação

O Python atribuira a variavel __name__ o valor __maian__ indicando que este modulo
e o modulo de execucao principal
"""

if __name__ == '__main__' :
    print("Estou rodando diretamente")

# isso so rodara se for executo este aquivo (dunder_main.py)
# se esse arquivo for importado não sera executado o que esta dentro do if acima