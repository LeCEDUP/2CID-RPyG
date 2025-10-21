from .personagem import Personagem

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo

# exemplo de criação de monstro
monstro1 = Monstro("Rola-bosta-africano", 500, 50, 150, "BOSTA")
monstro2 = Monstro("Pernilongo", 10, 500, 1, "DENGUE")
monstro3 = Monstro("Mosca-Fedida", 50 )
print("Nome:", monstro1.nome)
print("Vida:", monstro1.vida)
print("Ataque:", monstro1.ataque)
print("Defesa:", monstro1.defesa)
print("Tipo:", monstro1.tipo)