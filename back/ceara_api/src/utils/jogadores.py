import os
import django
import sys

# Adiciona o diretório 'src' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceara_api.settings')
django.setup()

# Importa o model
from core.models import Jogador

# Dados de exemplo
jogadores = [
    {"nome": "Bruno", "sobrenome": "Ferreira", "idade": 31, "posicao": "Goleiro"},
    {"nome": "Fernando", "sobrenome": "Miguel", "idade": 40, "posicao": "Goleiro"},
    {"nome": "Keiller", "sobrenome": "Silva", "idade": 28, "posicao": "Goleiro"},
    {"nome": "Richard", "sobrenome": "Oliveira", "idade": 34, "posicao": "Goleiro"},

    {"nome": "Éder", "sobrenome": "Ferreira", "idade": 30, "posicao": "Zagueiro"},
    {"nome": "Gabriel", "sobrenome": "Lacerda", "idade": 25, "posicao": "Zagueiro"},
    {"nome": "Luiz", "sobrenome": "Otávio", "idade": 36, "posicao": "Zagueiro"},
    {"nome": "Marcos", "sobrenome": "Victor", "idade": 23, "posicao": "Zagueiro"},
    {"nome": "Marllon", "sobrenome": "Gonçalves", "idade": 33, "posicao": "Zagueiro"},
    {"nome": "Ramon", "sobrenome": "Menezes", "idade": 30, "posicao": "Zagueiro"},
    {"nome": "Willian", "sobrenome": "Machado", "idade": 28, "posicao": "Zagueiro"},

    {"nome": "Diego", "sobrenome": "Fernandes", "idade": 29, "posicao": "Lateral"},
    {"nome": "Fabiano", "sobrenome": "Souza", "idade": 25, "posicao": "Lateral"},
    {"nome": "Matheus", "sobrenome": "Bahia", "idade": 25, "posicao": "Lateral"},
    {"nome": "Nicolas", "sobrenome": "Vecchiato", "idade": 28, "posicao": "Lateral"},
    {"nome": "Rafael", "sobrenome": "Ramos", "idade": 30, "posicao": "Lateral"},

    {"nome": "Fernando", "sobrenome": "Sobral", "idade": 30, "posicao": "Meio-Campista"},
    {"nome": "Lourenço", "sobrenome": "", "idade": 27, "posicao": "Meio-Campista"},
    {"nome": "Lucas", "sobrenome": "Lima", "idade": 25, "posicao": "Meio-Campista"},
    {"nome": "Lucas", "sobrenome": "Mugni", "idade": 33, "posicao": "Meio-Campista"},
    {"nome": "Matheus", "sobrenome": "Araújo", "idade": 23, "posicao": "Meio-Campista"},
    {"nome": "Richardson", "sobrenome": "", "idade": 33, "posicao": "Meio-Campista"},
    {"nome": "Rômulo", "sobrenome": "Azevedo", "idade": 23, "posicao": "Meio-Campista"},

    {"nome": "Alejandro", "sobrenome": "Martinez", "idade": 28, "posicao": "Atacante"},
    {"nome": "Aylon", "sobrenome": "", "idade": 33, "posicao": "Atacante"},
    {"nome": "Bruno", "sobrenome": "Tubarão", "idade": 30, "posicao": "Atacante"},
    {"nome": "Fernandinho", "sobrenome": "", "idade": 23, "posicao": "Atacante"},
    {"nome": "Antônio", "sobrenome": "Galeano", "idade": 25, "posicao": "Atacante"},
    {"nome": "Guilherme", "sobrenome": "Oliveira", "idade": 20, "posicao": "Atacante"},
    {"nome": "João", "sobrenome": "Victor", "idade": 21, "posicao": "Atacante"},
    {"nome": "Pedro", "sobrenome": "Henrique", "idade": 35, "posicao": "Atacante"},
    {"nome": "Pedro", "sobrenome": "Raul", "idade": 28, "posicao": "Atacante"},
]

# Populando o banco
for dados in jogadores:
    Jogador.objects.create(**dados)

print("Jogadores inseridos com sucesso.")
