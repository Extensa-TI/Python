"""
Dica de quando e onde tratar codigo:
TODA ENTRADA DEVE SER TRATADA!

# tratando erro generico (nao e a melhor pratica)
try:
    geek()
except:
    print("Deu algum problema aqui")

# tratando erro especifico
try:
    geek()
except NameError as err:
    print(f"Deu algum problema aqui: {err}")

try:
    geek()
except NameError as err:
    print(f"Deu algum problema aqui: {err}")
except TypeError as err:
    print(f"Deu algum problema aqui: {err}")
except:
    print("Deu algum problema aqui")

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}

print(pega_valor(dic, "nome"))
print(pega_valor(dic, "game"))
