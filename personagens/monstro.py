from personagem import Personagem

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo

# exemplo de criação de monstro
monstro1 = Monstro("Rola-bosta-africano", 500, 50, 150, "BOSTA")
monstro2 = Monstro("Pernilongo", 100, 200, 1, "DENGUE")
monstro3 = Monstro("Mosca-Fedida", 50, 20, 50, "PICADA MORTAL")
monstro4 = Monstro("Verme", 40, 30, 40, "CUSPE")
Monstro5 = Monstro("Besouro Blindado", 360, 75, 60, "CARAPAÇA DE FERRO", "Carapaça"),
Monstro6 = Monstro("Aranha Venenosa", 250, 95, 25, "VENENO LETAL", "Veneno"),
Monstro7 = Monstro("Louva-a-Deus Mutante", 300, 80, 35, "GOLPE CORTANTE", "Ataque Duplo")
print("Nome:", monstro1.nome)
print("Vida:", monstro1.vida)
print("Ataque:", monstro1.ataque)
print("Defesa:", monstro1.defesa)
print("Tipo:", monstro1.tipo)