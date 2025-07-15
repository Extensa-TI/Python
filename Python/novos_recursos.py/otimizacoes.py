import collections
from timeit import timeit
import sys

print('Todos apresentam melhorias em relação ap Python 3.7')
Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')
print(timeit('felicity.email', globals=globals()))
print(globals())
print()

print(sys.getsizeof(list(range(20250609))))
