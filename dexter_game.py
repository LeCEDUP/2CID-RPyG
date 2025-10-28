import random
import time
import sys

# ------------------------------
# Função para pausa com efeito
# ------------------------------
def pausa(texto, delay=1.8):
    """Imprime texto com pausa e flush para funcionar bem no terminal do VS Code"""
    print(texto)
    sys.stdout.flush()
    time.sleep(delay)

# ------------------------------
# CLASSE PRINCIPAL - DEXTER
# ------------------------------
class Dexter:
    def __init__(self):
        self.nome = "Dexter Morgan"
        self.vida = 100
        self.defesa = 10
        self.ataque = 25
        self.passageiro = 30
        self.xp = 0
        self.amostras = []
        self.descoberto = False

    def esta_vivo(self):
        return self.vida > 0
    def atacar(self, alvo):
        dano = max(5, random.randint(self.ataque - 5, self.ataque + 5) - alvo["defesa"])
        pausa(f"🩸 {self.nome} ataca {alvo['nome']} com precisão cirúrgica! Dano: {dano}")
        alvo["vida"] -= dano
        if alvo["vida"] <= 0:
            pausa(f"💀 {alvo['nome']} cai, sem vida.")
            return True
        else:
            # chance de contra-ataque
            if random.random() < 0.4:
                contra = max(3, random.randint(alvo["forca"] - 2, alvo["forca"] + 2) - self.defesa)
                self.vida -= contra
                pausa(f"⚔️ {alvo['nome']} revida! Dexter sofre {contra} de dano!")
            return False

    def sequestrar_e_levar(self, alvo):
        pausa(f"🕶️ {self.nome} segue {alvo['nome']} discretamente pela noite...")
        chance = random.random()
        if chance < 0.7:
            pausa("💉 Emboscada perfeita. O alvo é sedado e levado para a mesa.")
            self.ritual(alvo)
            return True
        else:
            pausa("🚨 O plano falha! O alvo reage e chama a polícia!")
            self.descoberto = True
            return False

    def ritual(self, alvo):
        pausa("🩸 Dexter cobre a sala com plástico... o som do mar ao fundo.")
        time.sleep(2)
        pausa(f"🔪 O ritual é executado. {alvo['nome']} encontra seu destino final.")
        self.xp += 75
        self.passageiro = max(0, self.passageiro - 15)
        self.amostras.append(alvo['nome'])


            def investigar(self, alvo):
        pausa(f"🕵️ {self.nome} investiga {alvo['nome']} nas sombras...")
        time.sleep(2)
        chance = random.random()

        if chance < 0.5:
            pausa(f"🔎 {alvo['nome']} possui um histórico violento... provas encontradas.")
            alvo["culpado"] = True
            alvo["defesa"] += 3
        elif chance < 0.8:
            pausa("❌ Nenhuma prova concreta. O Passageiro começa a sussurrar...")
            self.passageiro = min(100, self.passageiro + 10)
        else:
            pausa(f"🚨 {alvo['nome']} percebe que está sendo seguido!")
            if random.random() < 0.5:
                pausa("😨 Mas Dexter escapa sem ser visto.")
            else:
                pausa("👮 Alguém denuncia Dexter... ele está sob vigilância!")
                self.descoberto = True

    def descansar(self):
        pausa("😴 Dexter retorna ao laboratório para limpar vestígios e refletir.")
        self.vida = min(100, self.vida + 15)
        self.passageiro = max(0, self.passageiro - 5)
        if random.random() < 0.3:
            pausa("📞 Debra liga suspeitando de algo. A tensão aumenta...")
            self.passageiro += 5

    def estado(self):
        print("\n========================")
        print(f"🧠 Estado Mental: {self.estado_mental()}")
        print(f"❤️ Vida: {self.vida}")
        print(f"🩸 Passageiro Sombrio: {self.passageiro}")
        print(f"🔬 Amostras Coletadas: {len(self.amostras)}")
        print(f"🎯 Experiência: {self.xp}")
        print("========================")

    def estado_mental(self):
        if self.passageiro < 40:
            return "Controlado"
        elif self.passageiro < 70:
            return "Instável"
        else:
            return "À beira do colapso"
# ------------------------------
# LISTA DE VILÕES DA SÉRIE
# ------------------------------
viloes = [
    {"nome": "Ice Truck Killer", "vida": 70, "forca": 15, "defesa": 5, "inteligencia": 12, "culpado": True},
    {"nome": "Miguel Prado", "vida": 80, "forca": 18, "defesa": 8, "inteligencia": 15, "culpado": True},
    {"nome": "Doakes", "vida": 100, "forca": 20, "defesa": 10, "inteligencia": 20, "culpado": False},
    {"nome": "Jordan Chase", "vida": 85, "forca": 17, "defesa": 9, "inteligencia": 16, "culpado": True},
    {"nome": "Trinity Killer", "vida": 120, "forca": 25, "defesa": 12, "inteligencia": 22, "culpado": True},
]

