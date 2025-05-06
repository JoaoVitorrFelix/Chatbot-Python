import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'\n{nome}, vale muito a pena aprender Python. É uma das linguagens que mais cresce no mundo, com salários de R$2100 até mais de R$10.000 no Brasil, e média de $85.000/ano nos EUA.\n')
    elif resposta == '2':
        print(f'\n{nome}, isso depende do seu esforço. Algumas pessoas conseguem um emprego em 3 meses, outras levam mais tempo. O importante é praticar diariamente.\n')
    elif resposta == '3':
        print(f'\n{nome}, você sabe que está pronto quando entende os fundamentos e começa a construir projetos. Não espere estar "perfeito" para começar a aplicar para vagas.\n')
    elif resposta == '4':
        print(f'\n{nome}, você pode estudar grátis no YouTube, em livros e sites. Mas se quer algo mais estruturado, com projetos e suporte, recomendo o cursodepython.net.\n')
    elif resposta == '5':
        print(f'\n{nome}, os 5 pilares são: variáveis, estruturas de decisão, laços de repetição, funções e manipulação de dados.\n')
    elif resposta == '6':
        print(f'\n{nome}, sim! Python é considerada uma das melhores linguagens para iniciantes por sua simplicidade e legibilidade.\n')
    elif resposta == '7':
        print(f'\n{nome}, com Python você pode fazer automação, análise de dados, inteligência artificial, APIs, jogos, apps e muito mais.\n')
    elif resposta == '8':
        print(f'\n{nome}, sim! Python é excelente para automação de tarefas como organizar arquivos, enviar e-mails, preencher planilhas, entre outros.\n')
    elif resposta == '9':
        print(f'\n{nome}, sim! Com frameworks como Flask ou Django, é possível criar sites completos com Python.\n')
    elif resposta == '10':
        print(f'\n{nome}, as principais bibliotecas de dados são: pandas, numpy, matplotlib, seaborn e scikit-learn.\n')
    elif resposta == '11':
        print(f'\n{nome}, comece pelo básico: variáveis, loops, funções. Use sites como w3schools, Curso em Vídeo ou livros como "Automatize tarefas maçantes com Python".\n')
    elif resposta == '12':
        print(f'\n{nome}, sim! Python é uma das linguagens mais usadas em ciência de dados, junto com R e SQL.\n')
    elif resposta == '13':
        print(f'\n{nome}, treine resolvendo desafios em sites como HackerRank, CodeWars, ou criando pequenos projetos práticos.\n')
    elif resposta == '14':
        print(f'\n{nome}, Python é simples, multiplataforma, tem vasta comunidade, é versátil e possui milhares de bibliotecas úteis.\n')
    elif resposta == '15':
        print(f'\n{nome}, sim! Python suporta programação orientada a objetos, com classes, herança, encapsulamento e mais.\n')
    elif resposta == '16':
        print(f'\n{nome}, a comunidade Python é extremamente ativa, com fóruns, eventos, grupos e muita produção de conteúdo.\n')
    elif resposta == '17':
        print(f'\n{nome}, monte um portfólio com projetos simples e úteis: automações, API REST, CRUD com Flask, dashboards, etc. Suba no GitHub!\n')
    elif resposta == '18':
        print(f'\n{nome}, sim! Com a biblioteca Pygame, é possível criar jogos 2D com Python.\n')
    elif resposta == '19':
        print(f'\n{nome}, Python permite criar APIs facilmente com Flask, Django REST Framework, FastAPI e outras bibliotecas.\n')
    elif resposta == '20':
        print(f'\n{nome}, o mercado de Python é excelente, especialmente nas áreas de dados, automação, backend e inteligência artificial.\n')
    elif resposta == '0':
        print(f'\nAté logo, {nome}! Obrigado por usar o Chatbot Python.\n')
        exit()
    else:
        print('\nDigite apenas um número entre 0 e 20.\n')

def start():
    print('Olá! Bem-vindo ao chatbot Python desenvolvido pelo João Vitor Felix\n')
    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')
    while True:
        resposta = input(
            f'\nO que gostaria de saber hoje?\n'
            '[1] - Vale a pena aprender Python?\n'
            '[2] - Quanto tempo leva para conseguir um emprego com Python?\n'
            '[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?\n'
            '[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?\n'
            '[5] - Quais são os 5 pilares da programação com Python?\n'
            '[6] - Python é uma boa linguagem para iniciantes?\n'
            '[7] - O que dá pra fazer com Python?\n'
            '[8] - Dá pra automatizar tarefas com Python?\n'
            '[9] - Dá pra criar sites com Python?\n'
            '[10] - Quais bibliotecas usar para análise de dados com Python?\n'
            '[11] - Como começar a programar em Python?\n'
            '[12] - Posso usar Python em ciência de dados?\n'
            '[13] - Como treinar programação com Python?\n'
            '[14] - Quais são as principais características do Python?\n'
            '[15] - Python é orientado a objetos?\n'
            '[16] - A comunidade de Python é ativa?\n'
            '[17] - Como criar um portfólio com projetos Python?\n'
            '[18] - Dá pra fazer jogos com Python?\n'
            '[19] - Python permite criar APIs?\n'
            '[20] - O mercado de trabalho para Python está bom?\n'
            '[0] - Sair\n'
        )
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
