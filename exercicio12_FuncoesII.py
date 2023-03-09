# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplica(numero):
    return numero * 2

def triplica(numero):
    return numero *3


def quadruplica(numero):
    return numero *4


def multiplica(numero, fator):
    return numero*fator


numero = input('Digite um número: ')
numero_inteiro = int(numero)
fator = input('Digite o fator de multiplicação: ')
fator_inteiro = int(fator)

print('Os resultados são:')
print(f'{numero_inteiro} * 2 é {duplica(numero_inteiro)}')
print(f'{numero_inteiro} * 3 é {triplica(numero_inteiro)}')
print(f'{numero_inteiro} * 4 é {quadruplica(numero_inteiro)}')
print(f'{numero_inteiro} * {fator_inteiro} é {multiplica(numero_inteiro, fator_inteiro)}')