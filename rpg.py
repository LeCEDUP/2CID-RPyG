# Desenvolva o seu jogo aqui

from personagens.heroi import Heroi

def menu():
    print('---The Legend of the Cosmic Hunter---')
    print('-------------------------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    print('----------------------')
    nome_do_heroi = input('digite o nome do seu heroi')
meu_heroi = heroi(nome_do_heroi, 100, 20, 10)
from personagens.monstro import Monstro
from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura

Bounty_Hunter = Heroi("nome do heroi" 100, 15, 5)
Alien = Monstro("Alien", 30, 8, 2, "Médio")
Android = Monstro("Android", 30, 8, 2, "Grande")

Big_Bertha = Arma("arma de fogo", "Uma arma perigosa.", 10)
Traje_Pretor = Armadura("Escudo de Energia", "Um escudo resistente.", 5)
Redbull = Item("Poção de Vida", "Restaura 30 de vida.", 30)
#ele nao te da asas

print("--- Início da Aventura ---")

Bounty_Hunter.inventario.append(Arma)
Bounty_Hunter.inventario.append(Armadura)
Bounty_Hunter.inventario.append(Item)
print(f"{heroi.nome} encontrou uma {Arma.Big_Bertha}, um {Armadura.Traje_Pretor} e uma {Item.RedBull}.")
