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

def habilidade(self, inimigo):
    dano = self.ataque * 1.5
    inimigo.vida -= dano
    print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome}, causando {dano} de dano!")






