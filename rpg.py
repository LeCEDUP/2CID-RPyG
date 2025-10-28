from personagens.heroi import Heroi
from personagens.monstro import Monstro
from itens.arma import Arma
from itens.armadura import Armadura
from itens.item import Item
import random

# Configuração do jogo
heroi = Heroi(input("Nome do Caçador: "), 100, 15, 5)
drhokens = 100
planeta_atual = "Tatooine"
nivel_missao = 0

# Planetas disponíveis
planetas = {
    "Tatooine": {"dificuldade": 1, "recompensa": 1.0},
    "Coruscant": {"dificuldade": 2, "recompensa": 1.5},
    "Kashyyyk": {"dificuldade": 3, "recompensa": 2.0},
    "Mustafar": {"dificuldade": 4, "recompensa": 3.0}
}

# Inimigos por dificuldade
inimigos = [
    [Monstro("Alien Zergon", 50, 10, 3, "Alien"), Monstro("Mercenário", 60, 12, 4, "Humano")],
    [Monstro("Robô Assassino", 80, 15, 5, "Robô"), Monstro("Caçador Droide", 90, 16, 6, "Droide")],
    [Monstro("Wookie Fugitivo", 110, 18, 7, "Wookie"), Monstro("Jedi Caído", 120, 20, 8, "Jedi")],
    [Monstro("Lorde Sith", 150, 25, 10, "Sith"), Monstro("General Imperial", 140, 22, 9, "Imperial")]
]

# Bosses dos planetas
bosses = [
    Monstro("CHEFE: Gangster Hutt", 200, 30, 12, "Hutt"),
    Monstro("CHEFE: Mestre do Crime", 250, 35, 15, "Crime"),
    Monstro("CHEFE: Rei Wookie", 300, 40, 18, "Wookie"),
    Monstro("CHEFE: Imperador Sith", 400, 50, 25, "Sith")
]

