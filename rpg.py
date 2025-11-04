#rpg
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

heroi = Heroi("Lina", 100, 10, 4)
lobo = Monstro("Lobo Selvagem", 40, 8, 2, "Médio")
troll = Monstro("Troll das Montanhas", 120, 15, 6, "Grande")