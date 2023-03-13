# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('!!! Vamos testar seus conhecimentos !!!')
acertos = 0
total_questoes = len(perguntas)

for questoes in perguntas:
    #Separando as coisas de cada pergunta
    pergunta_atual = questoes.get('Pergunta')
    opcoes_atual = questoes.get('Opções')
    resposta_atual = questoes.get('Resposta')

    print(f'Pergunta: {pergunta_atual}')
    print()


    contador_opcao = range(len(opcoes_atual)) #Percorrendo a lista de opções
    for indice, nome in enumerate(opcoes_atual):
        print(f'{indice}){nome}')
        #Pegando a resposta do usuário
    print()
    resposta_usuario = input('Escolha uma opção: ')


    print()
    try:
        resposta_usuario_int = int(resposta_usuario)
    except:
        print('Digite uma opção válida! Reinicie o teste...')
        print()
        break
    
    if (resposta_usuario_int < len(opcoes_atual)) and (resposta_usuario_int >= 0):
        #verificando se a resposta está correta
        if opcoes_atual[resposta_usuario_int] == resposta_atual:
            print('Acertou 🎉')
            print()
            acertos += 1
        else:
            print('Errrrrrrrou 😧')
            print()
    else:
        print('Errrrrrrrou 🙄! Digite uma opção válida!')
        print()

print (f'Você acertou {acertos} de {total_questoes} questões!')
