# Desenvolva o seu jogo aqui
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

# ===========================
# 🔥 RPG DRAGON BALL 
# ===========================

print("🌌 --- BATALHA PELO UNIVERSO: DRAGON BALL SUPER --- 🌌")
print("Prepare-se para lutar pela sobrevivência de todos os universos!")

# Criando personagens
heroi = Heroi("Goku (Ultra Instinct)", 500, 70, 25)
jiren = Monstro("Jiren", 450, 85, 30, "Gigante")
black_freeza = Monstro("Black Freeza", 600, 90, 35, "Grande")
vegeta = Heroi("Vegeta (Ultra Ego)", 480, 75, 22)
# Criando itens
kamehameha = Arma("Kamehameha", "Golpe icônico de Goku, carregado com energia divina.", 40)
armadura_treinamento = Armadura("Gi de Treinamento do Whis", "Uniforme divino que aumenta a defesa.", 20)
senzu = Item("Semente dos Deuses", "Restaura completamente a vida.")

