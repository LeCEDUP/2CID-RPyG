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
            print(f"ATAQUE CRÍTICO de {self.nome}!")
        elif random.random() < 0.10:
            print(f"{alvo.nome} esquivou do ataque!")
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

    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} ganhou {exp} XP!")

        if self.experiencia >= self.experiencia_necessaria:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self._vida_maxima = VIDA_BASE_HEROI + (self.nivel - 1) * VIDA_POR_NIVEL
        self.vida = self._vida_maxima
        self.mana = MANA_BASE + (self.nivel - 1) * MANA_POR_NIVEL
        self.ataque += 5
        self.defesa += 2
        print(f"✨ {self.nome} subiu para o nível {self.nivel}! Vida e mana restauradas!")

    def lancar_magia(self, alvo):
        #Adiciona custo de mana
        custo = 10
        if self.mana < custo:
            print("Mana insuficiente!")
            return
        self.mana -= custo
        dano = random.randint(DANO_MAGIA_MIN, DANO_MAGIA_MAX)
        print(f"{self.nome} lança uma magia poderosa em {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def exibir_status(self):
        super().exibir_status()
        print(f"Nível {self.nivel} | XP: {self.experiencia}/{EXP_PARA_NIVEL} | Mana: {self.mana}/{MANA_BASE + (self.nivel - 1) * MANA_POR_NIVEL}")
        itens = [item.nome for item in self.inventario] or ["(vazio)"]
        print("Inventário:", ", ".join(itens))

# -------------------------
# MONSTRO
# -------------------------
class Monstro(Personagem):
    def __init__(self, nome, tipo):
        config = CONFIG_MONSTROS[tipo]
        super().__init__(nome, config["vida"], config["ataque"], config["defesa"])
        self.tipo = tipo
        self.exp_recompensa = config["exp_recompensa"]
        self.chance_loot = config["chance_loot"]

# -------------------------
# MENU DE BATALHA
# -------------------------
def menu_batalha(heroi, monstro):
    print(f"\nInício da batalha: {heroi.nome} vs {monstro.nome} ({monstro.tipo})")

    while heroi.esta_vivo() and monstro.esta_vivo():
        print("-" * 30)
        heroi.exibir_status()
        monstro.exibir_status()

        print("\n1️⃣ Atacar | 2️⃣ Magia | 3️⃣ Poção (não implementado aqui)")
        escolha = input("Escolha sua ação: ")

        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            heroi.lancar_magia(monstro)
        else:
            print("Ação inválida!")

        if monstro.esta_vivo():
            monstro.atacar(heroi)

    if heroi.esta_vivo():
        print(f"{heroi.nome} venceu e ganhou {monstro.exp_recompensa} XP!")
        heroi.ganhar_experiencia(monstro.exp_recompensa)
    else:
        print(f"{heroi.nome} foi derrotado...")

# -------------------------
# INÍCIO
# -------------------------
def main():
    print("🌟 Bem-vindo ao RPG Melhorado 🌟")
    nome = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome)
    monstro = Monstro("Goblin", "Pequeno")
    menu_batalha(heroi, monstro)

if __name__ == "__main__":
    main()

