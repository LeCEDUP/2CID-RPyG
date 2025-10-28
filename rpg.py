# Desenvolva o seu jogo aqui
import time

# ========================
# Classes de Itens e Personagens
# ========================

class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Arma(Item):
    def __init__(self, nome, descricao, bonus_ataque):
        super().__init__(nome, descricao)
        self.bonus_ataque = bonus_ataque

class Armadura(Item):
    def __init__(self, nome, descricao, bonus_defesa):
        super().__init__(nome, descricao)
        self.bonus_defesa = bonus_defesa

class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []

def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

 def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def equipar_item(self, item):
        if hasattr(item, "bonus_ataque"):
            self.ataque += item.bonus_ataque
        if hasattr(item, "bonus_defesa"):
            self.defesa += item.bonus_defesa
        print(f"{self.nome} equipou {item.nome}!")

    def ganhar_experiencia(self, exp):
        print(f"{self.nome} ganhou {exp} de experiência!")

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, tipo):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo
