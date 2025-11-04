class Monstro(Personagem):
    def _init_(self, nome, tipo, vida, ataque, defesa):
        super()._init_(nome, vida, ataque, defesa)
        self.tipo = tipo

    def _str_(self):
        return f"{self.nome} [{self.tipo}] (Vida: {self.vida}, Atq: {self.ataque}, Def: {self.defesa})"