# Desenvolva o seu jogo aqui TESTE 123

from itens.item import Item
from itens.arma import Arma
from itens.armadura import Armadura
from personagens.heroi import Heroi
from personagens.monstro import Monstro


class Guerreiro(Heroi):
    def __init__(self, nome):
        super().__init__(nome, vida=150, ataque=25, defesa=10)
        self.classe = "Guerreiro"






