for num in range(1,11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop')

while True:
    comando = input('Digite sair para encerrar! ')
    if comando == 'sair':
        break
    else:
        print(comando)
