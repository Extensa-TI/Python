"""
Usando lista

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums 

for n in fib_lista(100): # com 100000 utilizou 449,2 MB
    print(n)    
"""

def fib_gen(max):
    a, b, counter = 0, 1, 0
    while counter < max:    
        yield b
        a, b = b, a + b
        counter += 1

for n in fib_gen(100): # com 100000 utilizou 3,1 MB
    print(n)    





