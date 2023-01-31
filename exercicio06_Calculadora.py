while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-*/): ')
    
    numeros_validos = None
    num1 = 0
    num2 = 0
    resultado = 0
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_validos = '+-*/'
    
    if operador not in operadores_validos:
        print('Operador Inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizand sua conta, confira o resultado abaixo')

    if operador == '+':
        resultado = num1 + num2
        #print(f'{num1} {operador} {num2} = {resultado}')
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print('Nunca deveria chegar aqui')

    print(f'{num1} {operador} {num2} = {resultado}')


    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    print(sair)
    if sair is True:
        break