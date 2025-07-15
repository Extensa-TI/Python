"""
Dica de quando e onde tratar codigo:
TODA ENTRADA DEVE SER TRATADA!

else -> e executado somente quand se nao ocorre erro
finally -> e sempre executado e geralmente e utilizado para fechar ou desalocar recursos

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')
finally:
    print('Executando o finally')

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Nao e possivel dividir por zero'
    except:
        return 'Erro desconhecido'

num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))

"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto: {err}'
    except:
        return 'Erro desconhecido'

num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))



