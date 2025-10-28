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
