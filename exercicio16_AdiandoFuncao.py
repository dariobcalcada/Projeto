# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def potencia(x,y):
    return x**y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
potencia_de_dois = criar_funcao(potencia,2)
potencia_de_tres = criar_funcao(potencia,3)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
print(potencia_de_dois(3))
print(potencia_de_tres(2))