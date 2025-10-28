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
    meu_heroi = Mago(nome_heroi)

vampiro = Monstro("Vampiro", 160, 8, 2, "Pequeno")
troll = Monstro("Troll", 160, 22, 8, "Grande")


espada = Arma("Espada Longa", "Uma espada afiada.", 10)
escudo = Armadura("Escudo de Ferro", "Um escudo resistente.", 5)
pocao_vida = Item("Poção de Vida", "Restaura 30 de vida.")

meu_heroi.inventario.append(espada)
meu_heroi.inventario.append(escudo)
meu_heroi.inventario.append(pocao_vida)
print(f"{meu_heroi.nome} encontrou uma {espada.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

meu_heroi.equipar_item(espada)
meu_heroi.equipar_item(escudo)

def menu():
    print('----------------------')
    print('---Apocalipse Zumbi---')
    print('----------------------')
    print('Nas terras esquecidas de Eldarion, onde antigas ruínas ainda sussurram histórias de batalhas e glória, monstros voltaram a despertar das sombras.')
    print('Aldeias inteiras desapareceram, e o medo se espalha como uma névoa espessa.')
    print('Em meio ao caos, um grupo de guerreiros se ergue, unidos pelo destino e pela promessa de restaurar a paz')
    print('----------------------')

    print('---Início da aventura---')
    print(f"{meu_heroi.nome} encontrou uma {espada.nome}, um {escudo.nome} e uma {pocao_vida.nome}.")

    
    print("\n---Batalha contra o Vampiro---")
    while meu_heroi.esta_vivo() and vampiro.esta_vivo():
        escolha = input("Atacar ou usar habilidade? [a/h] ")
        if escolha.lower() == 'a':
            meu_heroi.atacar(vampiro)
        elif escolha.lower() == 'h':
            meu_heroi.habilidade(vampiro)

        if vampiro.esta_vivo():
            vampiro.atacar(meu_heroi)
            print(f"Vida de {meu_heroi.nome}: {meu_heroi.vida}")

        if pocao_vida in meu_heroi.inventario and meu_heroi.vida < 50:
            print(f"{meu_heroi.nome} usou {pocao_vida.nome} automaticamente!")
            meu_heroi.vida += 30
            if meu_heroi.vida > meu_heroi.vida:  
                meu_heroi.vida = meu_heroi.vida
            meu_heroi.inventario.remove(pocao_vida)
            print(f"Vida atual: {meu_heroi.vida}")

        if meu_heroi.esta_vivo():
          print(f"\n{meu_heroi.nome} derrotou o {vampiro.nome}!")
          meu_heroi.ganhar_experiencia(50)
          print(f"Vida de {meu_heroi.nome}: {meu_heroi.vida}")

        if meu_heroi.esta_vivo():
          print("\n---Nova batalha contra o Troll---")
          while meu_heroi.esta_vivo() and troll.esta_vivo():
            escolha = input("Atacar? [s/n] ")
            if escolha.lower() == 's':
                meu_heroi.atacar(troll)
                if troll.esta_vivo():
                    troll.atacar(meu_heroi)






