import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, na minha visão vale muito a pena, isso porque Python é uma das linguagens que mais cresce no mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil, além de contar com uma média anual de $85.000 dólares nos EUA.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo. Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe ou está disposto a correr atrás para aprender.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, ninguém vai te dizer magicamente que você está bom o suficiente. Quando dominar os fundamentos de Python, comece a aplicar para vagas e criar projetos reais.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, você pode estudar por vídeos gratuitos, livros, sites e cursos pagos. Uma boa recomendação é o cursodepython.net.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome}, os 5 pilares da programação com Python são: variáveis, estruturas condicionais, laços de repetição, funções e estruturas de dados (listas, dicionários, etc).{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep}{nome}, sim! Python é ótimo para quem está começando, pois possui uma sintaxe simples, legível e é muito versátil.{os.linesep}')
    elif resposta == '7':
        print(f'{os.linesep}{nome}, você pode usar Python para automação, análise de dados, desenvolvimento web, inteligência artificial, jogos, e muito mais.{os.linesep}')
    elif resposta == '8':
        print(f'{os.linesep}{nome}, sim! Com Python é possível automatizar tarefas como envio de e-mails, organização de arquivos, coleta de dados de sites e muito mais.{os.linesep}')
    elif resposta == '9':
        print(f'{os.linesep}{nome}, sim, com Python é possível criar sites usando frameworks como Django e Flask.{os.linesep}')
    elif resposta == '10':
        print(f'{os.linesep}{nome}, a biblioteca Pandas é muito utilizada para análise de dados em Python, assim como NumPy e Matplotlib.{os.linesep}')
    elif resposta == '11':
        print(f'{os.linesep}{nome}, para começar com Python, instale o Python do site oficial, use um editor como VS Code e comece com exercícios simples de lógica.{os.linesep}')
    elif resposta == '12':
        print(f'{os.linesep}{nome}, sim, Python é amplamente utilizado em ciência de dados e machine learning com bibliotecas como scikit-learn, TensorFlow e PyTorch.{os.linesep}')
    elif resposta == '13':
        print(f'{os.linesep}{nome}, você pode treinar resolvendo exercícios no HackerRank, Codewars, LeetCode ou projetos próprios como bots, sites ou scripts.{os.linesep}')
    elif resposta == '14':
        print(f'{os.linesep}{nome}, Python é uma linguagem interpretada e de alto nível, com forte tipagem dinâmica e suporte a múltiplos paradigmas (orientado a objetos, funcional, etc).{os.linesep}')
    elif resposta == '15':
        print(f'{os.linesep}{nome}, sim! Python tem suporte a orientação a objetos, permitindo criar classes, herança, encapsulamento, etc.{os.linesep}')
    elif resposta == '16':
        print(f'{os.linesep}{nome}, Python possui uma enorme comunidade ativa, com fóruns, tutoriais, repositórios no GitHub e respostas rápidas no Stack Overflow.{os.linesep}')
    elif resposta == '17':
        print(f'{os.linesep}{nome}, você pode versionar seus projetos com Git e publicar no GitHub, isso mostra sua evolução e ajuda no portfólio profissional.{os.linesep}')
    elif resposta == '18':
        print(f'{os.linesep}{nome}, sim, Python pode ser usado para desenvolver jogos simples com bibliotecas como Pygame.{os.linesep}')
    elif resposta == '19':
        print(f'{os.linesep}{nome}, sim, você pode desenvolver APIs com frameworks como Flask e FastAPI.{os.linesep}')
    elif resposta == '20':
        print(f'{os.linesep}{nome}, o mercado está muito aquecido para quem trabalha com Python, especialmente em áreas como automação, ciência de dados e web.{os.linesep}')
    else:
        print('Digite um número entre 1 e 20')

def start():
    print('Olá! Bem-vindo ao chatbot de perguntas e respostas desenvolvido pelo João Vitor Felix')
    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')
    while True:
        resposta = input(
    f'O que gostaria de saber hoje?{os.linesep}'
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
)

        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
