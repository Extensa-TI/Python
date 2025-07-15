import datetime

print('Maximo e Minimo de anos suportados pelo Python')
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print()

print('Retorna a data atual')
print(datetime.datetime.now())
print(repr(datetime.datetime.now()))
print()

print('replace()-> Ajustar a data e hora')
inicio = datetime.datetime.now()
inicio = inicio.replace(year=2026,month=12,day=30,hour=16, minute=0, second=0, microsecond=0)
print(inicio)
print()

print('criando uma data')
evento = datetime.datetime(2050,1,1, 0,0,0,0)
print(evento)
print()

print('Convertendo uma string data para datetime')
nascimento = '09/11/1960'
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print()

print('Acessando os dados individuais de data e hora')
evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

