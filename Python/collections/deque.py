"""
Modulo Collections - Deque
Lista de alto performance
"""
from collections import deque
deq = deque('Geek')
print(deq)

# append
deq.append('y')
print(deq)

# appendleft
deq.appendleft('k')
print(deq)

# pop
print(deq.pop()) # retorna o elemento deletado

# popleft
print(deq.popleft()) # retorna o elemento deletado
