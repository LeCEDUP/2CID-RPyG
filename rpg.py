#rpg
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro

heroi = Heroi("Lina", 100, 10, 4)
lobo = Monstro("Lobo Selvagem", 40, 8, 2, "Médio")
troll = Monstro("Troll das Montanhas", 120, 15, 6, "Grande")

espada = Arma("Espada de Madeira", "Uma espada simples feita à mão.", 4)
armadura = Armadura("Armadura de Couro", "Protege um pouco contra golpes leves.", 3)
pocao = Item("Poção de Cura", "Restaura 25 de vida.")

print("\n=== Início da Aventura ===")
print(f"O herói {heroi.nome} inicia sua jornada na floresta misteriosa!")

heroi.inventario.extend([espada, armadura, pocao])
print(f"{heroi.nome} encontrou uma {espada.nome}, uma {armadura.nome} e uma {pocao.nome}!")

heroi.equipar_item(espada)
heroi.equipar_item(armadura)