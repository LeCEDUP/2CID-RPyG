import random
import sys
import time

# -------------------------
# FUNÇÃO DE DIGITAÇÃO E INTRODUÇÃO
# -------------------------
def digitar(texto, atraso=0.04):
    """Mostra o texto com efeito de digitação"""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def introducao():
    digitar("🌌 Era uma vez em Eldoria, um reino tomado pelas trevas...")
    digitar("👑 Após a queda do antigo rei, criaturas sombrias começaram a surgir das florestas e cavernas.")
    digitar("⚔️ Você é o último descendente dos Guardiões da Luz, herdeiro de um poder esquecido há séculos.")
    digitar("💫 Sua missão: restaurar a paz em Eldoria, enfrentando monstros e dominando a magia antiga.")
    digitar("✨ O destino do reino agora depende da sua coragem...\n")

# -------------------------
# CONFIGURAÇÕES
# -------------------------
EXP_PARA_NIVEL = 30
VIDA_BASE_HEROI = 100
VIDA_POR_NIVEL = 25
ATAQUE_BASE_HEROI = 10
DEFESA_BASE_HEROI = 5
DANO_MAGIA_MIN = 15
DANO_MAGIA_MAX = 25
MANA_BASE = 40
MANA_POR_NIVEL = 10

CONFIG_MONSTROS = {
    "Pequeno": {"vida": 35, "ataque": 6, "defesa": 3, "exp_recompensa": 15, "chance_loot": 0.5},
    "Grande": {"vida": 65, "ataque": 12, "defesa": 5, "exp_recompensa": 30, "chance_loot": 0.7}
}

# -------------------------
# CLASSES BASE
# -------------------------
class Personagem:
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
            print(f"💀 {self.nome} foi derrotado!")

    def esta_vivo(self):
        return self.vida > 0

    def exibir_status(self):
        barra = "❤️" * int(self.vida / self._vida_maxima * 10)
        print(f"{self.nome} - Vida: {self.vida}/{self._vida_maxima} {barra}")

# -------------------------
# ITENS
# -------------------------
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

class Pocao(Item):
    def __init__(self, nome, descricao, cura):
        super().__init__(nome, descricao)
        self.cura = cura

# -------------------------
# HERÓI
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
        if self.experiencia >= EXP_PARA_NIVEL:
            self.experiencia -= EXP_PARA_NIVEL
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self._vida_maxima += VIDA_POR_NIVEL
        self.vida = self._vida_maxima
        self.mana = MANA_BASE + (self.nivel - 1) * MANA_POR_NIVEL
        self.ataque += 4
        self.defesa += 2
        print(f"✨ {self.nome} subiu para o nível {self.nivel}! (+Vida, +Ataque, +Defesa, +Mana)")

    def lancar_magia(self, alvo):
        custo = 10
        if self.mana < custo:
            print("❌ Mana insuficiente!")
            return
        self.mana -= custo
        dano = random.randint(DANO_MAGIA_MIN, DANO_MAGIA_MAX)
        print(f"🔮 {self.nome} lança uma magia poderosa em {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def usar_pocao(self):
        pocao = next((i for i in self.inventario if isinstance(i, Pocao)), None)
        if pocao:
            self.vida = min(self._vida_maxima, self.vida + pocao.cura)
            self.inventario.remove(pocao)
            print(f"🧪 {self.nome} usou {pocao.nome} e curou {pocao.cura} de vida!")
        else:
            print("❌ Nenhuma poção disponível!")

    def equipar_item(self, item):
        if isinstance(item, Arma):
            self.ataque += item.bonus_ataque
            print(f"{self.nome} equipou {item.nome}! (+{item.bonus_ataque} ataque)")
        elif isinstance(item, Armadura):
            self.defesa += item.bonus_defesa
            print(f"{self.nome} equipou {item.nome}! (+{item.bonus_defesa} defesa)")
        elif isinstance(item, Pocao):
            self.inventario.append(item)
            print(f"{self.nome} guardou uma poção: {item.nome}.")
        else:
            print(f"{item.nome} não pode ser usado agora.")

    def exibir_status(self):
        super().exibir_status()
        barra_mana = "🔷" * int(self.mana / (MANA_BASE + (self.nivel - 1) * MANA_POR_NIVEL) * 10)
        print(f"Nível {self.nivel} | XP: {self.experiencia}/{EXP_PARA_NIVEL} | Mana: {self.mana} {barra_mana}")
        itens = [item.nome for item in self.inventario] or ["(vazio)"]
        print("🎒 Inventário:", ", ".join(itens))

# -------------------------
# MONSTROS
# -------------------------
class Monstro(Personagem):
    def __init__(self, nome, tipo, nivel_heroi):
        config = CONFIG_MONSTROS[tipo]
        vida = config["vida"] + (nivel_heroi - 1) * 10
        ataque = config["ataque"] + (nivel_heroi - 1) * 2
        defesa = config["defesa"] + (nivel_heroi - 1)
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo
        self.exp_recompensa = config["exp_recompensa"]
        self.chance_loot = config["chance_loot"]

    def loot(self):
        if random.random() < self.chance_loot:
            if self.tipo == "Pequeno":
                return random.choice([
                    Pocao("Poção de Cura", "Restaura 20 de vida", 20),
                    Arma("Adaga Enferrujada", "Aumenta o ataque em 2", 2)
                ])
            else:
                return random.choice([
                    Armadura("Escudo Velho", "Aumenta a defesa em 3", 3),
                    Pocao("Poção Forte", "Restaura 40 de vida", 40)
                ])
        return None

# -------------------------
# MENU DE BATALHA
# -------------------------
def menu_batalha(heroi, monstro):
    print(f"\n⚔️ Início da batalha: {heroi.nome} vs {monstro.nome} ({monstro.tipo})")
    while heroi.esta_vivo() and monstro.esta_vivo():
        print("-" * 35)
        heroi.exibir_status()
        monstro.exibir_status()
        print("\n1️⃣ Atacar | 2️⃣ Magia | 3️⃣ Poção")
        escolha = input("Escolha sua ação: ")

        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            heroi.lancar_magia(monstro)
        elif escolha == "3":
            heroi.usar_pocao()
        else:
            print("❌ Escolha inválida!")
            continue

        if monstro.esta_vivo():
            monstro.atacar(heroi)

    if heroi.esta_vivo():
        print(f"🏆 {heroi.nome} derrotou {monstro.nome} e ganhou {monstro.exp_recompensa} XP!")
        heroi.ganhar_experiencia(monstro.exp_recompensa)
        loot = monstro.loot()
        if loot:
            print(f"💎 {monstro.nome} dropou {loot.nome}!")
            heroi.equipar_item(loot)
    else:
        print("☠️ Você foi derrotado!")

# -------------------------
# INÍCIO DO JOGO
# -------------------------
def main():
    introducao()
    digitar("🌟 Bem-vindo ao RPG Aprimorado 🌟\n")
    nome = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome)
    digitar(f"\nBoa sorte em sua jornada, {heroi.nome}! Que os deuses estejam com você.\n")

    inimigos = [
        ("Goblin", "Pequeno"),
        ("Orc", "Grande"),
        ("Goblin Líder", "Pequeno"),
        ("Orc Guerreiro", "Grande")
    ]

    for nome_m, tipo in inimigos:
        if not heroi.esta_vivo():
            break
        monstro = Monstro(nome_m, tipo, heroi.nivel)
        menu_batalha(heroi, monstro)

    if heroi.esta_vivo():
        print(f"🎖️ {heroi.nome} sobreviveu a todas as batalhas e alcançou o nível {heroi.nivel}!")
    else:
        print("💀 Fim da jornada...")

if __name__ == "__main__":
    main()
