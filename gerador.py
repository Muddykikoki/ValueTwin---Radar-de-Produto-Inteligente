import json
import random
from faker import Faker

fake = Faker("pt_BR")

# Categorias e palavras-chave de exemplo
categories_keywords = {
    "eletronicos": ["ventilador", "ar", "resfriamento", "TV", "monitor", "som"],
    "celulares": ["smartphone", "celular", "android", "ios", "chip", "camera"],
    "informatica": ["notebook", "mouse", "teclado", "monitor", "usb"],
    "eletrodomesticos": ["geladeira", "fogão", "micro-ondas", "cafeteira"],
    "moveis": ["mesa", "cadeira", "sofa", "guarda-roupa"],
    "ferramentas": ["furadeira", "chave", "martelo", "serra"],
    "games": ["videogame", "console", "controle", "jogo"],
    "audio": ["fone", "caixa de som", "microfone", "amplificador"],
}

store_names = [
    ("Loja Eletrônicos", "Eletro"),
    ("Tech Importados", "TechImp"),
    ("Casa & Som", "CasaSom"),
    ("Mundo Digital", "MDigital"),
    ("Oficina do Lar", "OfLar"),
    ("Conecta Games", "ConectG"),
    ("Audio Prime", "AudPrime"),
    ("InfoWorld", "InfoW")
]

products = []

for i in range(1, 2001):
    category = random.choice(list(categories_keywords.keys()))
    store = random.choice(store_names)
    keywords = random.sample(categories_keywords[category], k=3)
    product = {
        "id": i,
        "name": fake.catch_phrase(),
        "description": fake.sentence(nb_words=6),
        "price": round(random.uniform(50, 5000), 2),
        "ratings": {
            "comments": round(random.uniform(3.0, 5.0), 1),
            "technical": round(random.uniform(3.0, 5.0), 1),
            "reliability": round(random.uniform(3.0, 5.0), 1)
        },
        "delivery": random.randint(1, 10),
        "store": {
            "name": store[0],
            "shortName": store[1]
        },
        "category": category,
        "keywords": keywords
    }
    products.append(product)

# Salvar em arquivo JSON
file_path = "/mnt/data/produtos_realistas.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

file_path
