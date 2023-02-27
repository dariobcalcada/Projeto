"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

cpf_digitado = input('Digite seu CPF completo (somente números): ')

while True:

    if len(cpf_digitado) != 11:
        print('CPF com quantidade de dígitos errada')
        break
    
    try:
        cpf = int(cpf_digitado)

    except:    
        print('Favor digitar apenas números!')
        break
    
    #PEGANDO DIGITOS VERIFICADORES PARA POSTERIOR COMPARAÇÃO
    primeiroDV = int(cpf_digitado[9])
    segundoDV = int(cpf_digitado[10])

    # print(f'Este é o primeiro DV: {primeiroDV}')
    # print(f'Este é o segundo DV: {segundoDV}')

    d1 = int(cpf_digitado[0])
    d2 = int(cpf_digitado[1])
    d3 = int(cpf_digitado[2])
    d4 = int(cpf_digitado[3])
    d5 = int(cpf_digitado[4])
    d6 = int(cpf_digitado[5])
    d7 = int(cpf_digitado[6])
    d8 = int(cpf_digitado[7])
    d9 = int(cpf_digitado[8])

    soma1 = ((d1*10) + (d2*9) +(d3*8) + (d4*7) + (d5*6) + (d6*5) + (d7*4) + (d8*3) + (d9*2)) * 10
    rest1 = soma1 % 11
    if rest1 == 10:
        rest1 = 0
    
    dv1 = rest1

    if dv1 == primeiroDV:
        print('Primeiro dígito verificador válido!')
    else:
        print('CPF Inválido!')
        break
    
    soma2 = ((d1*11) + (d2*10) +(d3*9) + (d4*8) + (d5*7) + (d6*6) + (d7*5) + (d8*4) + (d9*3) + (dv1*2)) * 10
    rest2 = soma2 % 11
    if rest2 == 10:
        rest2 = 0
    
    dv2 = rest2

    if dv2 == segundoDV:
        print('Segundo dígito verificador válido!')
    else:
        print('CPF Inválido!')
        break    
    

    print(f'O CPF {cpf_digitado} é válido!')
    break




