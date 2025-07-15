import datetime
import timeit 
import functools


print('now() pode especificar um timezone')
agora = datetime.datetime.now()
print(agora)
print()

print('today() nao pode especificar um timezone')
hoje = datetime.datetime.today()
print(hoje)
print()

print('combine()')
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)),datetime.time())
print(manutencao)
print()

print('weekday() comeca com zero, sendo segunda-feira')
print(manutencao.weekday())
print()

nascimento = '09/11/1960'
aniversario = nascimento.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]),month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terca-feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em um sabado')
elif aniversario.weekday() == 6:
    print('Voce nasceu em um domingo')
print()

print('strftime() data para string')
print(hoje.strftime('%d/%m/%Y'))
print(hoje.strftime('%d/%m/%y'))
print(hoje.strftime('%d/%B/%Y'))
print(hoje.strftime('%d/%b/%Y'))
print()

print('strptime() string para data')
nascimento = datetime.datetime.strptime('09/11/1960', '%d/%m/%Y')
print(nascimento)
print()

print('time')
almoco = datetime.time(12,30,0)
print(almoco)

print('timeit marcando o tempo de execucao de codigo')
tempo = timeit.timeit('"-".join(str(n) for n in range(100))',number= 1000)
print(tempo)

print('timeit testando o tempo de execucao de uma funcao')

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste,2), number=1000))

        