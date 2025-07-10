import os
import django
import sys
from datetime import date

# Adiciona o diretório 'src' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceara_api.settings')
django.setup()

# Importa o model
from core.models import Museu

# Dados dos eventos do museu
eventos = [
    {"ano": 1914, "descricao": "Fundação do Ceará Sporting Club.", "titulo": "escudo1914"},
    {"ano": 1918, "descricao": "Primeiro Clássico-Rei oficial: Ceará 2x0 Fortaleza.", "titulo": "escudo1918"},
    {"ano": 1964, "descricao": "Conquista da Taça Brasil – Zona Norte-Nordeste.", "titulo": "escudo1964"},
    {"ano": 1994, "descricao": "Vice-campeão da Copa do Brasil.", "titulo": "escudo1994"},
    {"ano": 2015, "descricao": "1º título da Copa do Nordeste.", "titulo": "escudo2015"},
    {"ano": 2022, "descricao": "Quartas da Copa Sul-Americana — melhor campanha internacional.", "titulo": "escudo2022"},
    {"ano": 2023, "descricao": "Conquista da 47ª edição do Cearense e reformulação com base e estrangeiros.", "titulo": "escudo2023"},
    {"ano": 2024, "descricao": "Títulos Sub-15, 17 e 20 + criação do departamento feminino.", "titulo": "escudo2024"},
]

# Populando o banco
for evento in eventos:
    Museu.objects.create(
        titulo=evento["titulo"],
        descricao=evento["descricao"],
        ano=evento["ano"],
    )

print("Eventos do museu inseridos com sucesso.")