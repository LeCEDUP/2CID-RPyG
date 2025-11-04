from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro
import random

heroi = Heroi("Arthur", 100, 15, 5)

espada = Arma("Espada Longa", "Uma espada afiada.", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
pocao = Item("Poção de Vida", "Restaura 30 de vida.")

heroi.inventario += [espada, escudo, pocao]

heroi.equipar_item(espada)
heroi.equipar_item(escudo)

inimigos = [
    Monstro("Goblin", 40, 8, 2, "Pequeno"),
    Monstro("Orc", 80, 15, 4, "Médio"),
    Monstro("Dragão", 200, 30, 8, "Grande")
]

print("\n=== bem vindo à aventura de RPG ===\n")