"""
Diferenca de datas
"""
import datetime

hoje = datetime.datetime.now()
aniversario = datetime.datetime(2025, 11,9,0)
tempo_evento = aniversario - hoje
print(type(tempo_evento))
print(repr(tempo_evento))
print(tempo_evento)
print()

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
data_pagamento = data_compra + regra_boleto
print(data_pagamento)

