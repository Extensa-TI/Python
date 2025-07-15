"""
Decorators
- Sao funcoes
- envolvem outras funcoes e aprimoram seu comportamento
- Decorators tambem sao exemplos de funcoes de ordem superior
- Decorators tem uma sintese propria usando o simbolo @

# Decorator como funcoes (Sintense nao recomendada)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhece-lo!")
        funcao()
        print("Tenha um otimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo ao curso de Python")

teste = seja_educado(saudacao)
teste()

def raiva():
    print("EU TE ODEIO!")

raiva_educada = seja_educado(raiva)
raiva_educada()
"""

# Decorator com Syntax Sugar (Sintese recomendada)

def seja_educado_mesmo(funcao): # Função decoradora
    def sendo_mesmo():
        print("Foi um prazer conhece-lo!")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo

@seja_educado_mesmo # Decorator
def apresentando():
    print("Meu nome e Pedro")

apresentando()

@seja_educado_mesmo # Decorator
def dormir():
    print("Quero dormir...")

dormir()


