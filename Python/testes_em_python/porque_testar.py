"""
Testes automatizados
Por que testar?
- Reduzir bugs
- Garatem que novos recursos da sua aplicação não quebrem recursos antigos
- Garantem que bugs que foram corrigidos anteriormente continuam corrigidos.
- Garatem que a refatoração não tragam novos bugs

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)
- Os testes são escritos primeiro
- Escreve-se o mínimo suficiente para fazer o teste passar.
- Então refatora o código para realizar a funcionalidade e testa novamente
- Uma vez que o teste passe, o recurso é considerado completo
"""

class Gato:

    def __init__(self,nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')
felix.miar()
print(felix.nome)



