"""
"""
import time

gen_inicio = time.time()
print(sum(i for i in range(100000000)))
gen_tempo = time.time() - gen_inicio  # Tempo de execução 4.1s

list_inicio = time.time()
print(sum([i for i in range(100000000)]))   # Tempo de execução 5.2s
list_tempo = time.time() - list_inicio

print(f"Generator expression levou: {gen_tempo}")
print(f"List comprehension levou: {list_tempo}")