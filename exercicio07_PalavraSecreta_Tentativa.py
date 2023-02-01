"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'

#variavel auxiliar para mostrar as letras nas posições corretas
palavra_escondida = palavra_secreta
while True:

    letra_candidata = input('Digite uma letra: ') #entrada de uma letra
    
    tamanho = len(letra_candidata)
    if tamanho > 1: #verificação se apenas 1 letra foi digitada
        print('Você digitou mais de uma letra. Tente novamente!')
        continue
    elif tamanho == 0: #verificação de digitação de pelo menos 1 letra
        print('Digite pelo menos uma letra')
        continue

    
    #verificando letra por letra com while
    i = 0;
    while i < len(palavra_secreta):
        if letra_candidata == palavra_secreta[i]:
            palavra_escondida = palavra_escondida.replace(palavra_secreta[i], letra_candidata)
            i += 1
        else: 
            palavra_escondida = palavra_escondida.replace(palavra_secreta[i], '*') 
            i += 1
            
    
    #verificar se a palavra foi descoberta
    conta_asterisco = 0
    for caractere in palavra_escondida: #cria a variável caractere e verifica se ela é asterisco
        if caractere == '*':
            conta_asterisco += 1
    
    if conta_asterisco == 0:
        print(f' Parabéns! A Palavra Secreta é {palavra_secreta}')
        break
    else:
        print(f'palavra ainda escondida: {palavra_escondida}')
        continue  


            
        
