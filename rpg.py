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

def usar_pocao():
    global heroi, pocao
    if pocao in heroi.inventario:
        heroi.vida += 30
        heroi.inventario.remove(pocao)
        print(f"\n {heroi.nome} usou uma poção e recuperou 30 de vida! Vida atual: {heroi.vida}")
    else:
        print("\n Você não tem mais poções!")

def status():
    print(f"\n Vida: {heroi.vida}")
    print(f" Defesa: {heroi.defesa}")
    print(f" Ataque base: {heroi.ataque}")
    print(f" Inventário: {[item.nome for item in heroi.inventario]}\n")


for inimigo in inimigos:
    print(f"\n Um {inimigo.nome} apareceu! Prepare-se!\n")

    while heroi.esta_vivo() and inimigo.esta_vivo():
        print("\nO que deseja fazer?")
        print("1 - Atacar")
        print("2 - Usar Poção")
        print("3 - Ver Status")

        escolha = input("> ")

        if escolha == "1":
            heroi.atacar(inimigo)
            if inimigo.esta_vivo():
                inimigo.atacar(heroi)

        elif escolha == "2":
            usar_pocao()
            if inimigo.esta_vivo():
                inimigo.atacar(heroi)

        elif escolha == "3":
            status()
            continue