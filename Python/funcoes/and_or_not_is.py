ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, check seu e-mail.')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, check seu e-mail.')
else:
    print('Bem-vindo usuário!')

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, check seu e-mail.')
else:
    print('Bem-vindo usuário!')
