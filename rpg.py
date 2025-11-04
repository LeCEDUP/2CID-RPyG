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

print("\n--- Batalha 1: Lobo Selvagem ---")
while heroi.esta_vivo() and lobo.esta_vivo():
    heroi.atacar(lobo)
    if lobo.esta_vivo():
        lobo.atacar(heroi)

        print(f"{heroi.nome} venceu o {lobo.nome} e ganhou 40 de experiência!")
    heroi.ganhar_experiencia(40)

    print("\n--- Herói usa uma poção ---")
if pocao in heroi.inventario:
    heroi.vida += 25
    heroi.inventario.remove(pocao)
    print(f"{heroi.nome} usou {pocao.nome}. Vida atual: {heroi.vida}")

    print("\n--- Batalha 2: Troll das Montanhas ---")
while heroi.esta_vivo() and troll.esta_vivo():
    heroi.atacar(troll)
    if troll.esta_vivo():
        troll.atacar(heroi)

        if heroi.esta_vivo():
    print(f"\nParabéns, {heroi.nome}! Você derrotou o {troll.nome} e libertou o vale da escuridão!")
    heroi.ganhar_experiencia(100)

    else:
    print(f"\n{heroi.nome} foi derrotado pelo {troll.nome}. Fim da jornada.")