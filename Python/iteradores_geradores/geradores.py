"""
- Generatiors podem ser criados com funcoes geradoras
- Funcoes geradoras sao funcoes que utilizam a palavra reservada yield
- Generators podem ser criados com Expressoes Geradoras

Diferencas entre Funcoes e Generators Functions (Funcoes Geradoras)

-------------------------------------------------------------------------------
| Funcoes                              | Generators Functions                 |
-------------------------------------------------------------------------------
| Utilizam return                      | Utilizam yield                       |
| Retorna uma vez                      | Podem utilizar yield multiplas vezes |
| Quando executada, retorna um valor  | Quando executada, retorna um generator|
-------------------------------------------------------------------------------
"""

# Exemplo de Generator Function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# Uma Generator Function nao e um generator. Ela retorna um generator quando chamada    

gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print()

for n in conta_ate(10):
    print(n)