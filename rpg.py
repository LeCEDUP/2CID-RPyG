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

class Mago(Heroi):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=15, defesa=5)
        self.mana = 100
        self.classe = "Mago"

    def habilidade(self, inimigo):
        if self.mana >= 20:
            dano = self.ataque * 2
            inimigo.vida -= dano
            self.mana -= 20
            print(f"{self.nome} lança Bola de Fogo em {inimigo.nome}, causando {dano} de dano! Mana restante: {self.mana}")
        else:
            print(f"{self.nome} não tem mana suficiente para usar Bola de Fogo!")


print("Escolha a classe do seu herói:")
print("1 - Guerreiro")
print("2 - Mago")
escolha_classe = input("Digite o número da classe: ")

nome_heroi = input("Digite o nome do seu herói: ")

if escolha_classe == '1':
    meu_heroi = Guerreiro(nome_heroi)
else:






