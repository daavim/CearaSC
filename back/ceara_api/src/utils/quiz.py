import os
import django
import sys

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceara_api.settings')
django.setup()

# Importa os models
from core.models import Quiz, Pergunta, Alternativa

# Estrutura dos dados
quizzes_data = {
    "Estrutura e Estádios": [
        {
            "texto": "Qual é o nome oficial do estádio-sede do Ceará Sporting Club?",
            "alternativas": [
                ("Castelão", False),
                ("Presidente Vargas", False),
                ("Vovozão", True),
                ("Cidade Vozão", False),
            ]
        },
        {
            "texto": "Em que cidade está localizado o CT Luís Campos, conhecido como Cidade Vozão?",
            "alternativas": [
                ("Fortaleza", False),
                ("Maracanaú", False),
                ("Eusébio", False),
                ("Itaitinga", True),
            ]
        },
        {
            "texto": "Qual a capacidade aproximada do Ginásio Vozão?",
            "alternativas": [
                ("500", False),
                ("1.000", False),
                ("1.500", True),
                ("2.000", False),
            ]
        },
        {
            "texto": "Qual é o nome do estádio oficial do Ceará?",
            "alternativas": [
                ("Arena Castelão", False),
                ("Estádio Presidente Vargas", False),
                ("Carlos de Alencar Pinto", True),
                ("Estádio João Aranha", False),
            ]
        },
        {
            "texto": "Como é conhecido o centro de treinamento do Ceará?",
            "alternativas": [
                ("CT Fortaleza", False),
                ("Cidade Vozão", True),
                ("Território Vovô", False),
                ("Arena Alvinegra", False),
            ]
        },
    ],

    "Ídolos do Vozão": [
        {
            "texto": "Quem é considerado o maior artilheiro da história do Ceará?",
            "alternativas": [
                ("Sérgio Alves", False),
                ("Gildo", True),
                ("Mota", False),
                ("Marco Aurélio", False),
            ]
        },
        {
            "texto": "Qual zagueiro recente virou ídolo pela sua dedicação e liderança no Ceará?",
            "alternativas": [
                ("Carlindo", False),
                ("Luiz Otávio", True),
                ("Mauro Calixto", False),
                ("Gabriel Lacerda", False),
            ]
        },
        {
            "texto": "Qual técnico é conhecido como “O Soldado Alvinegro”?",
            "alternativas": [
                ("Lula Pereira", False),
                ("Eugênio Rabelo", False),
                ("Dimas Filgueiras", True),
                ("Léo Condé", False),
            ]
        },
    ],

    "Títulos e Conquistas": [
        {
            "texto": "Quantos títulos do Campeonato Cearense o Ceará conquistou até 2025?",
            "alternativas": [
                ("42", False),
                ("45", False),
                ("47", True),
                ("50", False),
            ]
        },
        {
            "texto": "Em quais anos o Ceará venceu a Copa do Nordeste?",
            "alternativas": [
                ("2015, 2020 e 2023", True),
                ("2014, 2019 e 2023", False),
                ("2015, 2018 e 2021", False),
                ("2013, 2015 e 2022", False),
            ]
        },
        {
            "texto": "Quantas vezes o Ceará conquistou o Campeonato Cearense?",
            "alternativas": [
                ("38", False),
                ("42", False),
                ("47", True),
                ("50", False),
            ]
        },
        {
            "texto": "Quantas vezes o Ceará foi campeão da Copa do Nordeste?",
            "alternativas": [
                ("1", False),
                ("2", False),
                ("3", True),
                ("4", False),
            ]
        },
        {
            "texto": "Contra qual time o Ceará venceu a final da Copa do Nordeste de 2023?",
            "alternativas": [
                ("Bahia", False),
                ("Fortaleza", False),
                ("Sport", True),
                ("Vitória", False),
            ]
        },
        {
            "texto": "Em que ano o Ceará foi vice-campeão da Copa do Brasil?",
            "alternativas": [
                ("1991", False),
                ("1994", True),
                ("2001", False),
                ("2011", False),
            ]
        },
    ],

    "Torcida e Públicos": [
        {
            "texto": "Qual foi o maior público pagante da história do Ceará em um jogo?",
            "alternativas": [
                ("59.838", False),
                ("63.908", True),
                ("55.227", False),
                ("60.068", False),
            ]
        },
        {
            "texto": "Em que competição ocorreu o jogo com maior público pagante do Ceará?",
            "alternativas": [
                ("Copa do Nordeste", False),
                ("Série B 2024", True),
                ("Copa do Brasil", False),
                ("Série A 2010", False),
            ]
        },
    ],

    "Clássicos e Rivalidades": [
        {
            "texto": "Qual é o nome dado ao clássico entre Ceará e Fortaleza?",
            "alternativas": [
                ("Clássico das Cores", False),
                ("Clássico da Paz", False),
                ("Clássico-Rei", True),
                ("Clássico do Nordeste", False),
            ]
        },
        {
            "texto": "Quantas vitórias o Ceará tem no Clássico da Paz contra o Ferroviário?",
            "alternativas": [
                ("70", False),
                ("90", False),
                ("120", False),
                ("140", True),
            ]
        },
    ],

    "Fundação e Identidade": [
        {
            "texto": "Em que data foi fundado o Ceará Sporting Club?",
            "alternativas": [
                ("1 de maio de 1915", False),
                ("2 de junho de 1914", True),
                ("3 de julho de 1913", False),
                ("4 de agosto de 1916", False),
            ]
        },
        {
            "texto": "Qual foi o primeiro nome do clube antes de se chamar Ceará Sporting Club?",
            "alternativas": [
                ("Fortaleza Sport Club", False),
                ("Porangabuçu Futebol Clube", False),
                ("Rio Branco Football Club", True),
                ("Barão do Ceará", False),
            ]
        },
        {
            "texto": "Por que o Ceará abandonou a cor roxa do uniforme original?",
            "alternativas": [
                ("Porque o rival também usava", False),
                ("Porque não gostavam da cor", False),
                ("Porque era difícil conseguir camisas roxas", True),
                ("Por decisão da federação", False),
            ]
        },
        {
            "texto": "Qual é o mascote do Ceará?",
            "alternativas": [
                ("Um leão", False),
                ("Um vovô de barba e bigode brancos", True),
                ("Um pescador", False),
                ("Um lampião do sertão", False),
            ]
        },
    ],

    "Competições Internacionais": [
        {
            "texto": "Qual foi o adversário do Ceará em sua primeira partida oficial vencida na Argentina?",
            "alternativas": [
                ("Boca Juniors", False),
                ("River Plate", False),
                ("Independiente", True),
                ("Rosario Central", False),
            ]
        },
        {
            "texto": "Qual time o Ceará derrotou em La Paz, quebrando um tabu na altitude?",
            "alternativas": [
                ("Bolívar", False),
                ("Jorge Wilstermann", False),
                ("The Strongest", True),
                ("Always Ready", False),
            ]
        },
        {
            "texto": "Quantos jogos o Ceará venceu na fase de grupos da Sul-Americana 2022?",
            "alternativas": [
                ("3", False),
                ("4", False),
                ("5", False),
                ("6", True),
            ]
        },
    ],

    "Momentos Históricos": [
        {
            "texto": "Quem foi o artilheiro do Ceará na campanha do tricampeonato de 1961 a 1963?",
            "alternativas": [
                ("Gildo", False),
                ("Carlito", False),
                ("Charuto", False),
                ("Ivan Carioca", True),
            ]
        },
        {
            "texto": "Qual jogador marcou o gol da virada contra o Santos no jogo 1000 de Pelé?",
            "alternativas": [
                ("Samuel", False),
                ("Jorge Costa", False),
                ("Da Costa", True),
                ("Mauro Calixto", False),
            ]
        },
    ],

    "Brasileirão": [
        {
            "texto": "Em que ano o Ceará conquistou o acesso à Série A após 16 anos?",
            "alternativas": [
                ("2007", False),
                ("2008", False),
                ("2009", True),
                ("2010", False),
            ]
        },
        {
            "texto": "Em que posição o Ceará terminou o Brasileirão de 2010?",
            "alternativas": [
                ("8º", False),
                ("12º", True),
                ("14º", False),
                ("16º", False),
            ]
        },
    ],
}

# Populando o banco de dados
for quiz_titulo, perguntas in quizzes_data.items():
    quiz = Quiz.objects.create(titulo=quiz_titulo, descricao="")
    for pergunta_data in perguntas:
        pergunta = Pergunta.objects.create(quiz=quiz, texto=pergunta_data["texto"])
        for alt_texto, correta in pergunta_data["alternativas"]:
            Alternativa.objects.create(pergunta=pergunta, texto=alt_texto, correta=correta)

print("Quizzes populados com sucesso.")
