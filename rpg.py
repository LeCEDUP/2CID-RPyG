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

def atacar(self, inimigo):
        dano = self.ataque + (self.arma.dano if self.arma else 0)
        print(f"{self.nome} ataca {inimigo.nome} causando {dano} de dano!")
        inimigo.receber_dano(dano)

        def receber_dano(self, dano):
            defesa_total = self.defesa + (self.armadura.defesa if self.armadura else 0)
            dano_final = max(0, dano - defesa_total)
            self.vida -= dano_final
            print(f"{self.nome} recebeu {dano_final} de dano. Vida: {self.vida}")
            