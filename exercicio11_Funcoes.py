# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numeros in args:
        total *= numeros #total = total * numeros
    return total


t1 = multiplica(1,2,3)
t2 = multiplica(2)
t3 = multiplica(2,10,100,1000)

print(t1)
print(t2)
print(t3)


def par_impar(x):
    if (x % 2 == 0):
        return f' {x} é par'
    else:
        return f' {x} é impar'
    

print(par_impar(2))
print(par_impar(5))
