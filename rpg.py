import random


EXP_PARA_NIVEL = 20
VIDA_BASE_HEROI = 100
VIDA_POR_NIVEL = 20
ATAQUE_BASE_HEROI = 10
DEFESA_BASE_HEROI = 5
DANO_MAGIA_MIN = 15
DANO_MAGIA_MAX = 25
MANA_BASE = 40
MANA_POR_NIVEL = 10


CONFIG_MONSTROS = {
    "Pequeno": {"vida": 30, "ataque": 5, "defesa": 2, "exp_recompensa": 15, "chance_loot": 0.5},
    "Grande": {"vida": 60, "ataque": 12, "defesa": 5, "exp_recompensa": 30, "chance_loot": 0.7}
}

# -------------------------
# CLASSES BASE
# -------------------------
class Personagem:
    """Classe base para todos os seres vivos no jogo."""
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self._vida_maxima = vida  
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        
        if random.random() < 0.15:
            dano = int((self.ataque - alvo.defesa) * 1.5)
            print(f"💥 ATAQUE CRÍTICO de {self.nome}!")
        elif random.random() < 0.10:
            print(f"🌀 {alvo.nome} esquivou do ataque!")
            return
        else:
            dano = max(1, self.ataque - alvo.defesa)

        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

    def esta_vivo(self):
        return self.vida > 0
    
    
    def exibir_status(self):
        barra = "❤️" * int(self.vida / self._vida_maxima * 10)
        print(f"{self.nome} - Vida: {self.vida}/{self._vida_maxima} {barra}")

# -------------------------
# HEROI
# -------------------------
class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome, VIDA_BASE_HEROI, ATAQUE_BASE_HEROI, DEFESA_BASE_HEROI)
        self.nivel = 1
        self.experiencia = 0
        self.mana = MANA_BASE
        self.inventario = []