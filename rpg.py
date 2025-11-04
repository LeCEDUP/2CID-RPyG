#rpg
class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome}: {self.descricao}"
    
class Arma(Item):
    def __init__(self, nome, descricao, dano):
       super().__init__(nome, descricao)
       self.dano = dano

class Armadura(Item):
    def __init__(self, nome, descricao, defesa):
        super().__init__(nome, descricao)
        self.defesa = defesa

class Heroi:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.experiencia = 0
        self.nivel = 1
        self.inventario = []
        self.arma = None
        self.armadura = None

def esta_vivo(self):
        return self.vida > 0