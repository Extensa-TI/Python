"""
Módulo Collections - Ordered Dict
"""

# Em dicionários a ordem não é garantida
from collections import OrderedDict

dict1 = {'a': 1, 'b': 1}
dict2 = {'b': 1, 'a': 1}

print(dict1 == dict2) # True -> a ordem não importa

odict1 = OrderedDict({'a': 1, 'b': 1}) 
odict2 = OrderedDict({'b': 1, 'a': 1})

print(odict1 == odict2) # False -> a ordem importa
